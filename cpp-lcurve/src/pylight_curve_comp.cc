#include "trm/lcurve.h"
#include "trm/buffer2d.h"
#include "trm/constants.h"

#ifdef _OPENMP
  #include <omp.h>
#endif

/** This routine computes the light curve corresponding to a particular
 * model and times defined by some data. Data with negative or zero errors
 * are skipped for speed, corresponding fit values are set = 0.
 * \param mdl   the model
 * \param data  the data defining the times
 * \param scale work out linear scale factors by svd or not. This will either be a single number for all components
 *              or a different one for each, depending upon the modle parameter iscale.
 * \param info  if true, it prints out array sizes to stderr
 * \param calc  the computed light curve
 * \lcstar1     the light curve of star1
 * \lcdisc     the light curve of star1
 * \lcedge     the light curve of star1
 * \lcspot     the light curve of star1
 * \lcstar2     the light curve of star1
 * \param wdwarf contribution of the white at phase 0.5
 * \param logg2  flux-weighted logg for star 2, CGS units
 * \param rv1 and rv2 are volume-averaged radii
 * This file is modified by lijiao
 */

void Lcurve::pylight_curve_comp(const Lcurve::Model& mdl,
                              double *time, double *expose, int *ndiv, int Tsize,
                              bool info,
                              double *calc, double *lcstar1, double *lcdisc,
                              double *lcedge, double *lcspot, double *lcstar2,
                              double& wdwarf,
                              double& logg1, double& logg2, double& rv1, double& rv2){


  double r1, r2;
  mdl.get_r1r2(r1, r2);
  double rl2 = 1.- Roche::xl12(mdl.q, mdl.spin2);
  if(r2 < 0)
      r2 = rl2;
  else if(r2 > rl2)
      throw Lcurve_Error("pylight_curve_comp: the secondary star is larger than its Roche lobe!");

  LDC ldc1 = mdl.get_ldc1();
  LDC ldc2 = mdl.get_ldc2();

  // Compute gravitational radius of star 1 if need be. An extra factor
  // of 4 saves multiplication in the innermost loops later
  double rlens1 = 0.;
  if(mdl.glens1){
      // Compute G(M1+M2), SI, and the separation a, SI.
      double gm = std::pow(1000.*mdl.velocity_scale,3)*mdl.tperiod*Constants::DAY/Constants::TWOPI;
      double a = std::pow(gm/Subs::sqr(Constants::TWOPI/Constants::DAY/mdl.tperiod),1./3.);
      rlens1 = 4.*gm/(1.+mdl.q)/a/Subs::sqr(Constants::C);
  }

  // Generate arrays over each star's face. Fine grids first:
  Subs::Buffer1D<Point> star1f, star2f, disc, edge, spot;
  set_star_grid(mdl, Roche::PRIMARY, true, star1f);
  if(info) std::cerr << "Number of points for star 1 (fine) = " << star1f.size() << std::endl;

  set_star_grid(mdl, Roche::SECONDARY, true, star2f);
  if(info) std::cerr << "Number of points for star 2 (fine) = " << star2f.size() << std::endl;

  set_star_continuum(mdl, star1f, star2f);

  // Now coarse grids
  Subs::Buffer1D<Point> star1c;
  if(mdl.nlat1f == mdl.nlat1c){
      star1c = star1f;
  }else{
      set_star_grid(mdl, Roche::PRIMARY, false, star1c);
  }
  if(info) std::cerr << "Number of points for star 1 (coarse) = "
                     << star1c.size() << std::endl;

  bool copy2 = (mdl.nlat2f == mdl.nlat2c) &&
      (!mdl.npole || r1 >= r2 || (mdl.nlatfill == 0 && mdl.nlngfill == 0));

  Subs::Buffer1D<Point> star2c;
  if(copy2){
      star2c = star2f;
  }else{
      set_star_grid(mdl, Roche::SECONDARY, false, star2c);
  }
  if(info) std::cerr << "Number of points for star 2 (coarse) = "
                     << star2c.size() << std::endl;

  if(mdl.nlat1c != mdl.nlat1f || !copy2)
      set_star_continuum(mdl, star1c, star2c);

  // Work out grid switching parameters
  Ginterp gint;
  gint.phase1 = mdl.phase1;
  gint.phase2 = mdl.phase2;
  gint.scale11 = gint.scale12 = gint.scale21 = gint.scale22 = 1.;

  std::cout << "lijiao test pylight_curve_comp.cc:  mdl.nlat1: " << mdl.nlat1f << std::endl;
  if(mdl.nlat1c != mdl.nlat1f){
      std::cout << "lijiao test pylight_curve_comp.cc comp_star1:  mdl.iangle " << mdl.iangle << std::endl;
      double ff = comp_star1(mdl.iangle, ldc1, 0.9999999999*mdl.phase1,
                             0., 1, mdl.q, mdl.beam_factor1,
                             mdl.velocity_scale, gint, star1f, star1c);
      double fc = comp_star1(mdl.iangle, ldc1, 1.0000000001*mdl.phase1,
                             0., 1, mdl.q, mdl.beam_factor1,
                             mdl.velocity_scale, gint, star1f, star1c);
      gint.scale11 = ff/fc;
      ff = comp_star1(mdl.iangle, ldc1, 1.-0.9999999999*mdl.phase1,
                      0., 1, mdl.q, mdl.beam_factor1, mdl.velocity_scale,
                      gint, star1f, star1c);
      fc = comp_star1(mdl.iangle, ldc1, 1.-1.0000000001*mdl.phase1,
                      0., 1, mdl.q, mdl.beam_factor1, mdl.velocity_scale,
                      gint, star1f, star1c);
      gint.scale12 = ff/fc;
  }

  if(!copy2){
      std::cout << "lijiao test pylight_curve_comp.cc comp_star2:  mdl.iangle " << mdl.iangle << std::endl;
      double ff = comp_star2(mdl.iangle, ldc2, 1-1.0000000001*mdl.phase2,
                             0., 1, mdl.q, mdl.beam_factor2,
                             mdl.velocity_scale, mdl.glens1, rlens1,
                             gint, star2f, star2c);
      double fc = comp_star2(mdl.iangle, ldc2, 1-0.9999999999*mdl.phase2,
                             0., 1, mdl.q, mdl.beam_factor2,
                             mdl.velocity_scale, mdl.glens1, rlens1,
                             gint, star2f, star2c);
      gint.scale21 = ff/fc;
      ff = comp_star2(mdl.iangle, ldc2, 1.0000000001*mdl.phase2, 0., 1,
                      mdl.q, mdl.beam_factor2, mdl.velocity_scale,
                      mdl.glens1, rlens1, gint, star2f, star2c);
      fc = comp_star2(mdl.iangle, ldc2, 0.9999999999*mdl.phase2, 0., 1,
                      mdl.q, mdl.beam_factor2, mdl.velocity_scale,
                      mdl.glens1, rlens1, gint, star2f, star2c);
      gint.scale22 = ff/fc;
  }

  if(mdl.add_disc){

      // set disc upper surface and outer edge
      Lcurve::set_disc_grid(mdl, disc);
      Lcurve::set_disc_edge(mdl, true, edge, false);

      if(info)
          std::cerr << "Number of points for the disc = " << disc.size()
                    << std::endl;

      std::vector<std::pair<double,double> > eclipses;

      // note that the inner radius of the disc is set equal to that of the
      // white dwarf if rdisc1 <= 0 while the outer disc is set equal to the
      // spot radius
      double rdisc1 = mdl.rdisc1 > 0. ? mdl.rdisc1 : r1;
      double rdisc2 = mdl.rdisc2 > 0. ? mdl.rdisc2 : mdl.radius_spot;

      if(mdl.opaque){

          // Apply eclipse by disc to star 1
          for(int i=0; i<star1f.size(); i++){
              eclipses =  Roche::disc_eclipse(mdl.iangle, rdisc1, rdisc2,
                                              mdl.beta_disc, mdl.height_disc,
                                              star1f[i].posn);
              for(int j=0; j<eclipses.size(); j++)
                  star1f[i].eclipse.push_back(eclipses[j]);
          }
          for(int i=0; i<star1c.size(); i++){
              eclipses =  Roche::disc_eclipse(mdl.iangle, rdisc1, rdisc2,
                                              mdl.beta_disc, mdl.height_disc,
                                              star1c[i].posn);
              for(int j=0; j<eclipses.size(); j++)
                  star1c[i].eclipse.push_back(eclipses[j]);
          }

          // Apply eclipse by disc to star 2
          for(int i=0; i<star2f.size(); i++){
              eclipses =  Roche::disc_eclipse(mdl.iangle, rdisc1, rdisc2,
                                              mdl.beta_disc, mdl.height_disc,
                                              star2f[i].posn);
              for(int j=0; j<eclipses.size(); j++)
                  star2f[i].eclipse.push_back(eclipses[j]);
          }
          for(int i=0; i<star2c.size(); i++){
              eclipses =  Roche::disc_eclipse(mdl.iangle, rdisc1, rdisc2,
                                              mdl.beta_disc, mdl.height_disc,
                                              star2c[i].posn);
              for(int j=0; j<eclipses.size(); j++)
                  star2c[i].eclipse.push_back(eclipses[j]);
          }
      }

      // Set the surface brightness of the disc
      set_disc_continuum(rdisc2, mdl.temp_disc, mdl.texp_disc,
                         mdl.wavelength, disc);

      // Set the surface brightness of outer edge, accounting for
      // irradiation by star 2
      set_edge_continuum(mdl.temp_edge, r2, std::abs(mdl.t2),
                         mdl.absorb_edge, mdl.wavelength, edge);

  }

  // This could raise an exception for bad parameters.
  if(mdl.add_spot) Lcurve::set_bright_spot_grid(mdl, spot);

  // polynomial fudge factor stuff: slope, quad, cube
  double xmin = time[0], xmax = time[0];
  for(int np=1; np<Tsize; np++){
      xmin = time[np] > xmin ? xmin : time[np];
      xmax = time[np] < xmax ? xmax : time[np];
  }
  double middle = (xmin+xmax)/2., range = (xmax-xmin)/2.;

  // Compute light curve

  // Next use a dynamically-scheduled openmp section to speed the loop over the
  // data. Dynamic scheduling allows for variability in the time per point.
  // which is very likely to be the case. However, since the time per point is
  // large, overheads should not be too bad.

#ifdef _OPENMP
  int mxth = std::min(16, omp_get_max_threads());
  omp_set_num_threads(mxth);
#pragma omp parallel for schedule(dynamic) if(Tsize > 4)
#endif

  for(int np=0; np<Tsize; np++){

      // Compute phase, accounting for quadratic term
      double phase  = (time[np]-mdl.t0)/mdl.period;

      // small Newton-Raphson iteration
      for(int it=0; it<4; it++){
          phase -= (mdl.t0+phase*(mdl.period+mdl.pdot*phase)-time[np])/
              (mdl.period+2.*mdl.pdot*phase);
      }

      // advance/retard by time offset between primary & secondary eclipse
      phase += mdl.deltat/mdl.period/2.*(std::cos(2.*Constants::PI*phase)-1.);

      double exposei = expose[np]/mdl.period;
      double frac = (time[np]-middle)/range;
      double slfac  = 1. + frac*(mdl.slope+frac*(mdl.quad+frac*mdl.cube));
      if(mdl.iscale){
          lcstar1[np] = slfac*comp_star1(mdl.iangle, ldc1, phase, exposei,
                                         ndiv[np], mdl.q,
                                         mdl.beam_factor1, mdl.velocity_scale,
                                         gint, star1f, star1c);

          lcdisc[np] = slfac*comp_disc(mdl.iangle, mdl.lin_limb_disc,
                                       mdl.quad_limb_disc, phase, exposei,
                                       ndiv[np], mdl.q,
                                       mdl.velocity_scale, disc);

          lcedge[np] = slfac*comp_edge(mdl.iangle, mdl.lin_limb_disc,
                                       mdl.quad_limb_disc, phase, exposei,
                                       ndiv[np], mdl.q,
                                       mdl.velocity_scale, edge);

          lcspot[np] = slfac*comp_spot(mdl.iangle, phase, exposei,
                                         ndiv[np], mdl.q,
                                         mdl.velocity_scale, spot);

          if(mdl.t2 > 0)
              lcstar2[np] = slfac*comp_star2(mdl.iangle, ldc2, phase, exposei,
                                              ndiv[np], mdl.q,
                                              mdl.beam_factor2,
                                              mdl.velocity_scale,
                                              mdl.glens1, rlens1,
                                              gint, star2f, star2c);

      }else{
          calc[np] = slfac*comp_light(mdl.iangle, ldc1, ldc2,
                                      mdl.lin_limb_disc, mdl.quad_limb_disc,
                                      phase, exposei, ndiv[np],
                                      mdl.q, mdl.beam_factor1, mdl.beam_factor2,
                                      mdl.spin1, mdl.spin2, mdl.velocity_scale,
                                      mdl.glens1, rlens1, gint, star1f, star2f,
                                      star1c, star2c, disc, edge, spot) + mdl.third;
      }
  }

  // Compute white dwarf contribution
  Subs::Buffer1D<Point> fstar2;
  wdwarf = comp_star1(mdl.iangle, ldc1, 0.5, 0., 1, mdl.q, mdl.beam_factor1,
                      mdl.velocity_scale, gint, star1f, star1c);

  // calculate flux-weighted loggs and volume-averaged radii
  logg1 = comp_gravity1(mdl, star1f);
  logg2 = comp_gravity2(mdl, star2f);
  rv1 = comp_radius1(star1f);
  rv2 = comp_radius2(star2f);

  return;
}
