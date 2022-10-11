import numpy as np
from ctypes import *
import os, sys

libdir = os.path.abspath(__file__)
libdir = os.path.join(os.path.dirname(libdir), 'lib')


class lcurve:

    def __init__(self, libdir=libdir, lib='libpylcurve.so'):
        '''
        load libpylcurve
        '''
        libpylcurve=CDLL(f"{libdir}/{lib}")
        self.libpylcurve = libpylcurve

    def lc(self, times, expose=0, ndiv=1,
       ###Binary and stars
       q_value = 0.9670,  q_range = 0.,  q_dstep = 0.,  q_vary = False,  q_defined = False,
       iangle_value = 86.5063,  iangle_range = 0.,  iangle_dstep = 0.,  iangle_vary = False,  iangle_defined = False,
       r1_value = 0.006292,  r1_range = 0.,  r1_dstep = 0.,  r1_vary = False,  r1_defined = False,
       r2_value = 0.097168,  r2_range = 0.,  r2_dstep = 0.,  r2_vary = False,  r2_defined = False,
       cphi3_value = 0.015,  cphi3_range = 0.,  cphi3_dstep = 0.,  cphi3_vary = False,  cphi3_defined = False,
       cphi4_value = 0.017,  cphi4_range = 0.,  cphi4_dstep = 0.,  cphi4_vary = False,  cphi4_defined = False,
       spin1_value = 1.,  spin1_range = 0.,  spin1_dstep = 0.,  spin1_vary = False,  spin1_defined = False,
       spin2_value = 1.,  spin2_range = 0.,  spin2_dstep = 0.,  spin2_vary = False,  spin2_defined = False,
       teff1_value = 15918.02,  teff1_range = 0.,  teff1_dstep = 0.,  teff1_vary = False,  teff1_defined = False,
       teff2_value =  34570.39,  teff2_range = 0.,  teff2_dstep = 0.,  teff2_vary = False,  teff2_defined = False,
       ldc1_1_value = 0.81760,  ldc1_1_range = 0.,  ldc1_1_dstep = 0.,  ldc1_1_vary = False,  ldc1_1_defined = False,
       ldc1_2_value = -0.6685,  ldc1_2_range = 0.,  ldc1_2_dstep = 0.,  ldc1_2_vary = False,  ldc1_2_defined = False,
       ldc1_3_value = 0.6119,  ldc1_3_range = 0.,  ldc1_3_dstep = 0.,  ldc1_3_vary = False,  ldc1_3_defined = False,
       ldc1_4_value = -0.2362,  ldc1_4_range = 0.,  ldc1_4_dstep = 0.,  ldc1_4_vary = False,  ldc1_4_defined = False,
       ldc2_1_value = 0.8177,  ldc2_1_range = 0.,  ldc2_1_dstep = 0.,  ldc2_1_vary = False,  ldc2_1_defined = False,
       ldc2_2_value = -0.9078,  ldc2_2_range = 0.,  ldc2_2_dstep = 0.,  ldc2_2_vary = False,  ldc2_2_defined = False,
       ldc2_3_value = 0.7550,  ldc2_3_range = 0.,  ldc2_3_dstep = 0.,  ldc2_3_vary = False,  ldc2_3_defined = False,
       ldc2_4_value = -0.2518,  ldc2_4_range = 0.,  ldc2_4_dstep = 0.,  ldc2_4_vary = False,  ldc2_4_defined = False,
       velocity_scale_value = 323.4547,  velocity_scale_range = 0.,  velocity_scale_dstep = 0.,  velocity_scale_vary = False,  velocity_scale_defined = False,
       beam_factor1_value = 2.,  beam_factor1_range = 0.,  beam_factor1_dstep = 0.,  beam_factor1_vary = False,  beam_factor1_defined = False,
       beam_factor2_value = 1.3131,  beam_factor2_range = 0.,  beam_factor2_dstep = 0.,  beam_factor2_vary = False,  beam_factor2_defined = False,
       ##//General
       t0_value = 1.2012e-5,  t0_range = 0.,  t0_dstep = 0.,  t0_vary = False,  t0_defined = False,
       period_value = 1.,  period_range = 0.,  period_dstep = 0.,  period_vary = False,  period_defined = False,
       pdot_value = 0.,  pdot_range = 0.,  pdot_dstep = 0.,  pdot_vary = False,  pdot_defined = False,
       deltat_value = 0.,  deltat_range = 0.,  deltat_dstep = 0.,  deltat_vary = False,  deltat_defined = False,
       gravity_dark1_value = 0.44796,  gravity_dark1_range = 0.,  gravity_dark1_dstep = 0.,  gravity_dark1_vary = False,  gravity_dark1_defined = False,
       gravity_dark2_value = 0.44796,  gravity_dark2_range = 0.,  gravity_dark2_dstep = 0.,  gravity_dark2_vary = False,  gravity_dark2_defined = False,
       absorb_value = 1.,  absorb_range = 0.,  absorb_dstep = 0.,  absorb_vary = False,  absorb_defined = False,
       slope_value = 0.,  slope_range = 0.,  slope_dstep = 0.,  slope_vary = False,  slope_defined = False,
       quad_value = 0.,  quad_range = 0.,  quad_dstep = 0.,  quad_vary = False,  quad_defined = False,
       cube_value = 0.,  cube_range = 0.,  cube_dstep = 0.,  cube_vary = False,  cube_defined = False,
       third_value = 0.,  third_range = 0.,  third_dstep = 0.,  third_vary = False,  third_defined = False,
       ##// Star spots
       stsp11_long_value = 0.,  stsp11_long_range = 0.,  stsp11_long_dstep = 0.,  stsp11_long_vary = False,  stsp11_long_defined = False,
       stsp11_lat_value = 0.,  stsp11_lat_range = 0.,  stsp11_lat_dstep = 0.,  stsp11_lat_vary = False,  stsp11_lat_defined = False,
       stsp11_fwhm_value = 0.,  stsp11_fwhm_range = 0.,  stsp11_fwhm_dstep = 0.,  stsp11_fwhm_vary = False,  stsp11_fwhm_defined = False,
       stsp11_tcen_value = 0.,  stsp11_tcen_range = 0.,  stsp11_tcen_dstep = 0.,  stsp11_tcen_vary = False,  stsp11_tcen_defined = False,
       stsp21_long_value = 0.,  stsp21_long_range = 0.,  stsp21_long_dstep = 0.,  stsp21_long_vary = False,  stsp21_long_defined = False,
       stsp21_lat_value = 0.,  stsp21_lat_range = 0.,  stsp21_lat_dstep = 0.,  stsp21_lat_vary = False,  stsp21_lat_defined = False,
       stsp21_fwhm_value = 0.,  stsp21_fwhm_range = 0.,  stsp21_fwhm_dstep = 0.,  stsp21_fwhm_vary = False,  stsp21_fwhm_defined = False,
       stsp21_tcen_value = 0.,  stsp21_tcen_range = 0.,  stsp21_tcen_dstep = 0.,  stsp21_tcen_vary = False,  stsp21_tcen_defined = False,
       ##// disc
       rdisc1_value = 0.0,  rdisc1_range = 0.,  rdisc1_dstep = 0.,  rdisc1_vary = False,  rdisc1_defined = False,
       rdisc2_value = 0.,  rdisc2_range = 0.,  rdisc2_dstep = 0.,  rdisc2_vary = False,  rdisc2_defined = False,
       height_disc_value = 0.,  height_disc_range = 0.,  height_disc_dstep = 0.,  height_disc_vary = False,  height_disc_defined = False,
       beta_disc_value = 0.,  beta_disc_range = 0.,  beta_disc_dstep = 0.,  beta_disc_vary = False,  beta_disc_defined = False,
       temp_disc_value = 0.,  temp_disc_range = 0.,  temp_disc_dstep = 0.,  temp_disc_vary = False,  temp_disc_defined = False,
       texp_disc_value = 0.,  texp_disc_range = 0.,  texp_disc_dstep = 0.,  texp_disc_vary = False,  texp_disc_defined = False,
       lin_limb_disc_value = 0.,  lin_limb_disc_range = 0.,  lin_limb_disc_dstep = 0.,  lin_limb_disc_vary = False,  lin_limb_disc_defined = False,
       quad_limb_disc_value = 0.,  quad_limb_disc_range = 0.,  quad_limb_disc_dstep = 0.,  quad_limb_disc_vary = False,  quad_limb_disc_defined = False,
       temp_edge_value = 0.,  temp_edge_range = 0.,  temp_edge_dstep = 0.,  temp_edge_vary = False,  temp_edge_defined = False,
       absorb_edge_value = 0.,  absorb_edge_range = 0.,  absorb_edge_dstep = 0.,  absorb_edge_vary = False,  absorb_edge_defined = False,
       ##//Bright-spot
       radius_spot_value = 0.,  radius_spot_range = 0.,  radius_spot_dstep = 0.,  radius_spot_vary = False,  radius_spot_defined = False,
       length_spot_value = 0.,  length_spot_range = 0.,  length_spot_dstep = 0.,  length_spot_vary = False,  length_spot_defined = False,
       height_spot_value = 0.,  height_spot_range = 0.,  height_spot_dstep = 0.,  height_spot_vary = False,  height_spot_defined = False,
       expon_spot_value = 0.,  expon_spot_range = 0.,  expon_spot_dstep = 0.,  expon_spot_vary = False,  expon_spot_defined = False,
       epow_spot_value = 0.,  epow_spot_range = 0.,  epow_spot_dstep = 0.,  epow_spot_vary = False,  epow_spot_defined = False,
       angle_spot_value = 0.,  angle_spot_range = 0.,  angle_spot_dstep = 0.,  angle_spot_vary = False,  angle_spot_defined = False,
       yaw_spot_value = 0.,  yaw_spot_range = 0.,  yaw_spot_dstep = 0.,  yaw_spot_vary = False,  yaw_spot_defined = False,
       temp_spot_value = 0.,  temp_spot_range = 0.,  temp_spot_dstep = 0.,  temp_spot_vary = False,  temp_spot_defined = False,
       tilt_spot_value = 0.,  tilt_spot_range = 0.,  tilt_spot_dstep = 0.,  tilt_spot_vary = False,  tilt_spot_defined = False,
       cfrac_spot_value = 0.,  cfrac_spot_range = 0.,  cfrac_spot_dstep = 0.,  cfrac_spot_vary = False,  cfrac_spot_defined = False,
       ##Computational parameters
       delta_phase = 1.e-7,  nlat1f = 50,  nlat2f = 210,  nlat1c = 50,  nlat2c = 170,  npole = True,
       nlatfill = 3,  nlngfill = 2,  lfudge = 0.07,  llo = 0.,  lhi = -50.,  phase1 = 0.482,  phase2 = 0.018,  nrad = 40,  wavelength = 600.,
       roche1 = False,  roche2 = True,  eclipse1 = True,  eclipse2 = True,  glens1 = True,  use_radii=1.,
       tperiod = 0.40373,  gdark_bolom1 = 0.,  gdark_bolom2 = 0.,  mucrit1 = 0.,  mucrit2 = 0.,
       slimb1 = 'Claret', slimb2 = 'Claret',  mirror = False,  add_disc = False,  opaque = False,  add_spot = False,  nspot = 100,  iscale = False,
       info = False
       ):
        '''
        q_value = 0.12,  q_range = 0.01,  q_dstep = 0.0001,  q_vary = False,  q_defined = True,
        iangle_value = 82,  iangle_range = 2,  iangle_dstep = 0.01,  iangle_vary = True,  iangle_defined = True,
        r1_value = 0.17,  r1_range = 0.05,  r1_dstep = 0.001,  r1_vary = True,  r1_defined = True,
        .
        .
        .
        etc. The above would mean that q is not to be varied (as the penultimate q_vary=False), but iangle and r1 are. For simplex, genetic, simann
        and powell the *_range parameter specifies the range over which to vary the respective parameter (i.e. 0.01, 2 and 0.05 in this case),
        while the *_dstep parameter is used by levmarq to compute numerical derivatives using finite differences. Be careful to set this small enough
        to give accurate derivatives but not so small that roundoff will be problematic. It should, at a minimum, be smaller than the uncertainty in
        any parameter. The *_defined parameter is a relatively recent addition which specifies whether a given parameter is used at all and is designed for
        the star spot parameters. Here is the full list of parameters.
        parameters:
        ----------------------------------------------------------------------------------------------------------------------------------------------------
        times [float array 1D] --- it must be 1D np.array
        expose [float array 1D] --- The exposure length in the same units as the time
        ndiv [int or int array 1D] --- Factor to split up data points to allow for finite exposures
             Note: Time, expose,and ndiv arraies must have the same size
        !!!!Binary and stars!!!------------------
        q	---	Mass ratio, q = M2/M1
        iangle	---	Inclination angle, degrees
        r1	---	Radius of star 1, scaled by the binary separation
        r2	---	Radius of star 2, scaled by the binary separation. The radius is measured along the line of centres towards star 1. Set = -1 and hold fixed for Roche lobe filling stars.
        cphi3	---	Third contact phase (star 1 starting to emerge from eclipse). This is an alternative way to specify the radii, based on a spherical approximation fot the two stars, i.e. unless the stars are spherical, it is not quite the true third contact. The radii will be computed from the contact phases according to the two equations r2+r1 = sqrt(1 - sin^2 i cos^2 (2*pi*cphi4)) and r2-r1 = sqrt(1 - sin^2 i cos^2 (2*pi*cphi3)). The radii returned are precise, just the interpretation as contact phases that is not precise. cphi3 and cphi4 need the boolean use_radii set to 0 to enabled. The reason for using them is to help with MCMC iterations as they prevent the nasty curved correlation between r1, r2 and i. This can save a huge amount of CPU time.
        cphi4	---	Fourth contact phase, star 1 fully emerged from eclipse. See cphi3 for details.
        spin1	---	This is the ratio of the spin frequency of star 1 to the orbital frequency. In this case a modified form of the Roche potential is used for star 1
        spin2	---	This is the ratio of the spin frequency of star 2 to the orbital frequency. In this case a modified form of the Roche potential is used for star 2
        teff1	---	Temperature of star 1, Kelvin. This is really a substitute for surface brightness which is set assuming a black-body given this parameter. If it was not for irradiation that would be exactly what this is, a one-to-one replacement for surface brightness. Irradiation however introduces bolometric luminosities effectively and breaks the direct link. Some would then argue that one must use model atmospheres except at the moment irradiated model atmosphere are in their infancy.
        teff2	---	Temperature of star 2, Kelvin. Set < 0 in order that it does not get scaled when using the iscale parameter.
        ldc1_1, etc	---	Limb darkening for stars is quite hard to specify precisely. Here we adopt a 4 coefficient approach which can either represent a straighforward polynimal expanion of the form I(mu) = 1 - \sum_i a_i (1-mu)^i, or rather better in some cases Claret's 4-coefficient formula I(mu) = 1 - \sum_i a_i (1 - mu^(i/2)) (i=1 to 4). You specify these by supplying the 4 coefficients for each star (which for form's sake are potentially variable but you would probably be unwise to let them be free) and later on a parameter to say whether it is the polynomial or Claret's representation. The polynomial allows one to use linear and quadratic limb darkening amongst others by setting the upper coefficients = 0. ldc1_1 is the first coefficient of star 1, ldc1_2 is the second, etc, while ldc2_1 is the first coefficient for star 2 etc. See limb1, limb2, mucrit1, mucrit2 below.
        velocity_scale	---	Velocity scale, sum of unprojected orbital speeds, used for accounting for Doppler beaming and gravitational lensing. On its own this makes little difference to the light curve, so you should not usually let it be free, but you might want to if you have independent K1 or K2 information which you can apply as part of a prior.
        beam_factor1	---	The factor to use for Doppler beaming from star 1. This corresponds to the factor (3-alpha) that multiplies -v_r/c in the standard beaming formula where alpha is related to the spectral shape. Use of this parameter requires the velocity_scale to be set.
        beam_factor2	---	The factor to use for Doppler beaming from star 2. This corresponds to the factor (3-alpha) that multiplies -v_r/c in the standard beaming formula where alpha is related to the spectral shape. Use of this parameter requires the velocity_scale to be set.
        !!!General!!!-------------------------
        t0	---	Zero point of ephemeris, marking time of mid-eclipse (or in general superior conjunction) of star 1, same units as times.
        period	---	Orbital period, same units as times.
        pdot	---	Quadratic coefficient of ephemeris, same units as times
        deltat	---	Time shift between the primary and secondary eclipses to allow for small eccentricities and Roemer delays in the orbit. The sign is defined such that deltat > 0 implies that the secondary eclipse suffers a delay compared to the primary compared to precisely 0.5 difference. deltat < 0 implies the secondary eclipse comes a little earlier than expected. Assuming that the "primary eclipse" is the eclipse of star 1, then, using the same sign convention, the Roemer delay is given by = P*(K1-K2)/(Pi*c) where P is the orbital period, K1 and K2 are the usual projected radial velocity semi-amplitudes Pi = 3.14159.., and c = speed of light. See Kaplan (2010) for more details. The delay is implemented by adjusting the orbital phase according to phi' = phi + (deltat/2/P)*(cos(2*Pi*phi)-1), i.e. there is no change at primary eclipse but a delay of -deltat/P by the secondary eclipse.
        gravity_dark	---	Gravity darkening coefficient. Only matters for the Roche distorted case, but is prompted for always. There are two alternatives for this. In the standard old method, the temperatures on the stars are set equal to t2*(g/gr)**gdark where g is the gravity at a given point and gr is the gravity at the point furthest from the primary (the 'backside' of the secondary). For a convectuive atmosphere, 0.08 is the usual value while 0.25 is the number for a radiative atmosphere. This is translated into intensity using a blackbody approx. If you want to bypass the BB approx and invoke a direct relation flux ~ (g/gr)**gdark relation you should set gdark_bolom (see below) to 0 (false.)
        absorb	---	The fraction of the irradiating flux from star 1 absorbed by star 2
        slope, quad, cube	---	Fudge factors to help cope with any trends in the data as a result of e.g. airmass effects. The fit is multiplied by (1+x*(slope+x*(quad+x*cube))) where x is the time scaled so that it varies from -1 to 1 from start to end of the data. One should expect these number to have absolute value << 1.
        third	---	Third light contribution. Simply adds to whatever flux is calculated and will be subject to auto-scaling like other flux. It only applies if global scaling rather than individual component scaling is used. Third light is assumed strictly constant and is not subject to the slope, quad, cube parameters.
        !!!!Spots!!!--------------------------
        One spot allowed on each star (with some expectation that the number may be increased if need be in the future):
        stsp11_long	---	Longitude (degrees) of spot 1 on star 1, relative to meridian defined by line of centres
        stsp11_lat	---	Latitude (degrees) of spot 1 on star 1
        stsp11_lat	---	FWHM (degrees) of spot 1 on star 1, as seen from its centre of mass. Spot has gaussian distribution of temperature.
        stsp11_tcen	---	Central temp (K) of spot 1 on star 1
        stsp21_long	---	Longitude (degrees) of spot 1 on star 2, relative to meridian defined by line of centres
        stsp21_lat	---	Latitude (degrees) of spot 1 on star 2
        stsp21_lat	---	FWHM (degrees) of spot 1 on star 2, as seen from its centre of mass. Spot has gaussian distribution of temperature.
        stsp21_tcen	---	Central temp (K) of spot 1 on star 2
        !!!Disc!!!---------------------------
        rdisc1	---	Inner radius of azimuthally symmetric disc. Set = -1 to set it equal to r1 (it should not be allowed to vary in this case)
        rdisc2	---	Outer radius of azimuthally symmetric disc. Set = -1 and hold fixed to clamp this to equal the bright spot radius.
        height_disc	---	Half height of disc at radius = 1. The height varies as a power law of radius
        beta_disc	---	Exponent of power law in radius of disc. Should be >= 1 to make concave disc; convex will not eclipse properly.
        temp_disc	---	Temperature of outer part of disc. This is little more than a flux normalisation parameter but it is easier to think in terms of temperature
        texp_disc	---	Exponent of surface brightness (NB: not temperature) over disc
        lin_limb_disc	---	Linear limb darkening coefficient of the disc
        quad_limb_disc	---	Quadratic limb darkening coefficient of the disc
        temp_edge	---	Temperature at perpendicular edge of disc. Irradiation from the secondary is allowed so you should think of a bright rim at primary eclipse. Limb darkeining parameters of the disc are applied
        absorb_edge	---	Amount of secondary flux absorbed and reprocessed. This effect should lead to a sinusoidal variation with flux maximum at orbital phase 0.5. It was introduced to model a possible accreting sdO/WD system discovered by Thomas Kupfer
        !!!Bright-spot!!!---------------------
        radius_spot	---	Distance from accretor of bright-spot (units of binary separation).
        length_spot	---	Length scale of spot (units of binary separation).
        height_spot	---	Height of spot (units of binary separation). This is only a normalisation constant.
        expon_spot	---	Spot is modeled as x**n*exp(-(x/l)**m). This parameter specifies the exponent 'n'
        epow_spot	---	This is the exponent m in the above expression
        angle_spot	---	This is the angle made by the line of elements of the spot measured in the direction of binary motion relative to the rim of the disc so that the "standard" value should be 0.
        yaw_spot	---	Allows the spot elements effectively to beam their light away from the perpendicular to the line of elements. Measured as an angle in the same sense as angle_spot. 0 means standard perpendicular beaming.
        temp_spot	---	Normalises the surface brightness of the spot.
        tilt_spot	---	Allows spot to be other than perpendicular to the disc. 90 = perpendicular. If less than 90 then the spot is visible for more than half a cycle.
        cfrac_spot	---	The fraction of the spot taken to be equally visible at all phases, i.e. pointing upwards.
        !!!Computational parameters!!!--------------------
        delta_phase [float] ---	Accuracy in phase of eclipse computations. This determines the accuracy of any Roche computations. Example: 1.e-7
        nlat1f [int] --- The number of latitudes for star 1's fine grid. This is used around the phase of primary eclipse (i.e. the eclipse of star 1
        nlat1c [int] --- The number of latitudes for star 1's coarse grid. This is used away from primary eclipse.
        nlat2f [int] --- The number of latitudes for star 2's fine grid. This is used around the phase of secondary eclipse.
        nlat2c [int] --- The number of latitudes for star 2's coarse grid. This is used away from secondary eclipse.
        npole [bool] --- True to set North pole of grid to the genuine stellar NP rather than substellar points. This is probably a good idea when modelling well detached binaries, especially with extreme radius ratios because then it allows one to concentrate points over a band of latitudes using the next two parameters
        nlatfill [int] --- Extra number of points to insert per normal latitude strip along the path of star 1 as it transits star 2. This is designed to help tough extreme radius ratio cases. Take care to look at the resulting grid with visualise as the exact latitude range chosen is a little approximate. This is only enabled if npole since only then do the latitude strips more-or-less line up with the movement of the star.
        nlngfill [int] --- Extra number of points to insert per normal longitude strip along the path of star 1 as it transits star 2. This is designed to help tough extreme radius ratio cases. Take care to look at the resulting grid with visualise as the exact latitude range chosen is a little approximate.
        lfudge [float] --- The fine-grid latitude strip is computed assuming both stars are spherical. To allow for departures from this, this parameter allows one to increase the latitude limits both up and down by an amount specified in degrees. Use the program visualise to judge how large this should be. However, one typically would like to avoid lfudge > 30*r1/r2 as that could more than double the width of the strip.
        llo, lhi [float] --- These are experimental. They allow the user to fix the latitude limits of the fine strip which might be useful in preventing chi**2 variations caused by variable grids. The values need to reflect the likely range of inclinations and can only really be set by trial and error using visualise. They are in degrees following the usual convention for latitude on Earth. Set llo high and lhi low to stop them having any effect.
        phase1 [float] --- this defines when star 1's fine grid is used abs(phase) < phase1. Thus phase1 = 0.05 will restrict the fine grid use to phase 0.95 to 0.05.
        phase2 [float] --- this defines when star 2's fine grid is used phase2 until 1-phase2. Thus phase2 = 0.45 will restrict the fine grid use to phase 0.55 to 0.55.
        nrad [int] --- The number of radial strips over the disc
        wavelength [float] --- Wavelength (nm)
        roche1 [bool] --- Account for Roche distortion of star 1 or not
        roche2 [bool] --- Account for Roche distortion of star 2 or not
        eclipse1 [bool] --- Account for the eclipse of star 1 or not
        eclipse2 [bool] --- Account for the eclipse of star 2 or not
        glens1 [float] --- Account for gravitational lensing by star 1. If you use this roche1 must be = 0 and the velocity_scale
        use_radii [float] --- If set = True, the parameters r1 and r2 will be used to set the radii directly. If not, the third and fourth contact phases, cphi3 and cphi4, will be used instead (see description for cphi3 for details).
        tperiod [float] --- The true orbital period in days. This is required, along with velocity_scale, if gravitational lensing is being applied to calculate proper dimensions in the system.
        gdark_bolom [float] --- True if the gravity darkening coefficient represents the bolometric value where T is proportional to gravity to the power set by the coefficient. This is translated to flux variations using the black-body approximation. If False, it represents a filter-integrated value 'y' coefficient such that the flux depends upon the gravity to the power 'y'. This is itself an approximation and ideally should replaced by a proper function of gravity, but is probably good enough for most purposes. Please see gravity_dark.
        mucrit1 [float] --- Critical value of mu on star 1 below which intensity is assumed to be zero. This is to allow one to represent Claret and Hauschildt's (2004) results where I(mu) drops steeply for mu < 0.08 or so. WARNING: this option is dangerous. I would normally advise setting it = 0 unless you really know what you are doing as it leads to discontinuities.
        mucrit2 [float] --- Critical value of mu on star 2 below which intensity is assumed to be zero. See comments on mucrit1 for more.
        slimb1 [stri] --- String, either 'Poly' or 'Claret' determining the type of limb darkening law. See comments on ldc1_1 above.
        slimb2 [stri] --- String, either 'Poly' or 'Claret' determining the type of limb darkening law. See comments on ldc1_1 above.
        mirror [bool] --- Add any light not reprocessed in as if star reflected it or not as a crude approximation to the effet of gray scattering
        add_disc [bool] --- Add a disc or not
        opaque [bool] --- Make disc opaque or not
        iscale [bool] --- Individually scale the separate components or not. If set the each component, star 1, star 2, disc and bright spot will be individually scaled to minimise chi**2. Otherwise a single overall factor will be computed. NB If you set this parameter then all temperature parameters (white dwarf, secondary, disc and bright spot) must be held fixed otherwise near-total degeneracy will result. The only reason it is not total is because of reflection effect from irradiation of the secondary by the white dwarf, but this is often very feeble and will not help, so, you have been warned. Scaling should in general lead to faster convergence than not scaling. You may have some cases where you do not want to include any secondary star component. You can do this by setting t2 < 0. Note that if this is set true, then the third light parameter will be ignored.
        info [bool] --- if true, it prints out array sizes to stderr
        returns:
        ----------------------------------------------------------------------------------------------------------------------------------------------------
        '''
        Tsize = len(times)
        ####--------------inintalize time and light curves arrays-----------------------------------------
        if isinstance(expose, float): expose = expose*np.ones(Tsize, dtype=np.double)
        if isinstance(ndiv, float): ndiv = ndiv*np.ones(Tsize, dtype=np.int)
        calc, lcstar1, lcdisc, lcedge, lcspot, lcstar2 = np.empty((6, Tsize), dtype=np.float)
        ####----------------------- declare variables------------------------------------------------------
        times = times.ctypes.data_as(POINTER(c_double*Tsize))
        expose = expose.ctypes.data_as(POINTER(c_double*Tsize))
        ndiv = ndiv.ctypes.data_as(POINTER(c_int*Tsize))
        calc = calc.ctypes.data_as(POINTER(c_double*Tsize))
        lcstar1 = lcstar1.ctypes.data_as(POINTER(c_double*Tsize))
        lcdisc = lcdisc.ctypes.data_as(POINTER(c_double*Tsize))
        lcedge = lcedge.ctypes.data_as(POINTER(c_double*Tsize))
        lcspot = lcspot.ctypes.data_as(POINTER(c_double*Tsize))
        lcstar2 = lcstar2.ctypes.data_as(POINTER(c_double*Tsize))
        Tsize = c_int(Tsize)
        #### Binary and stars
        q_value, q_range, q_dstep, q_vary,  q_defined = c_double(q_value), c_double(q_range), c_double(q_dstep), c_bool(q_vary), c_bool(q_defined)
        iangle_value, iangle_range, iangle_dstep, iangle_vary,  iangle_defined = c_double(iangle_value), c_double(iangle_range), c_double(iangle_dstep), c_bool(iangle_vary), c_bool(iangle_defined)
        r1_value, r1_range, r1_dstep, r1_vary,  r1_defined = c_double(r1_value), c_double(r1_range), c_double(r1_dstep), c_bool(r1_vary), c_bool(r1_defined)
        r2_value, r2_range, r2_dstep, r2_vary,  r2_defined = c_double(r2_value), c_double(r2_range), c_double(r2_dstep), c_bool(r2_vary), c_bool(r2_defined)
        cphi3_value, cphi3_range, cphi3_dstep, cphi3_vary,  cphi3_defined = c_double(cphi3_value), c_double(cphi3_range), c_double(cphi3_dstep), c_bool(cphi3_vary), c_bool(cphi3_defined)
        cphi4_value, cphi4_range, cphi4_dstep, cphi4_vary,  cphi4_defined = c_double(cphi4_value), c_double(cphi4_range), c_double(cphi4_dstep), c_bool(cphi4_vary), c_bool(cphi4_defined)
        spin1_value, spin1_range, spin1_dstep, spin1_vary,  spin1_defined = c_double(spin1_value), c_double(spin1_range), c_double(spin1_dstep), c_bool(spin1_vary), c_bool(spin1_defined)
        spin2_value, spin2_range, spin2_dstep, spin2_vary,  spin2_defined = c_double(spin2_value), c_double(spin2_range), c_double(spin2_dstep), c_bool(spin2_vary), c_bool(spin2_defined)
        teff1_value, teff1_range, teff1_dstep, teff1_vary,  teff1_defined = c_double(teff1_value), c_double(teff1_range), c_double(teff1_dstep), c_bool(teff1_vary), c_bool(teff1_defined)
        teff2_value, teff2_range, teff2_dstep, teff2_vary,  teff2_defined = c_double(teff2_value), c_double(teff2_range), c_double(teff2_dstep), c_bool(teff2_vary), c_bool(teff2_defined)
        ldc1_1_value, ldc1_1_range, ldc1_1_dstep, ldc1_1_vary,  ldc1_1_defined = c_double(ldc1_1_value), c_double(ldc1_1_range), c_double(ldc1_1_dstep), c_bool(ldc1_1_vary), c_bool(ldc1_1_defined)
        ldc1_2_value, ldc1_2_range, ldc1_2_dstep, ldc1_2_vary,  ldc1_2_defined = c_double(ldc1_2_value), c_double(ldc1_2_range), c_double(ldc1_2_dstep), c_bool(ldc1_2_vary), c_bool(ldc1_2_defined)
        ldc1_3_value, ldc1_3_range, ldc1_3_dstep, ldc1_3_vary,  ldc1_3_defined = c_double(ldc1_3_value), c_double(ldc1_3_range), c_double(ldc1_3_dstep), c_bool(ldc1_3_vary), c_bool(ldc1_3_defined)
        ldc1_4_value, ldc1_4_range, ldc1_4_dstep, ldc1_4_vary,  ldc1_4_defined = c_double(ldc1_4_value), c_double(ldc1_4_range), c_double(ldc1_4_dstep), c_bool(ldc1_4_vary), c_bool(ldc1_4_defined)
        ldc2_1_value, ldc2_1_range, ldc2_1_dstep, ldc2_1_vary,  ldc2_1_defined = c_double(ldc2_1_value), c_double(ldc2_1_range), c_double(ldc2_1_dstep), c_bool(ldc2_1_vary), c_bool(ldc2_1_defined)
        ldc2_2_value, ldc2_2_range, ldc2_2_dstep, ldc2_2_vary,  ldc2_2_defined = c_double(ldc2_2_value), c_double(ldc2_2_range), c_double(ldc2_2_dstep), c_bool(ldc2_2_vary), c_bool(ldc2_2_defined)
        ldc2_3_value, ldc2_3_range, ldc2_3_dstep, ldc2_3_vary,  ldc2_3_defined = c_double(ldc2_3_value), c_double(ldc2_3_range), c_double(ldc2_3_dstep), c_bool(ldc2_3_vary), c_bool(ldc2_3_defined)
        ldc2_4_value, ldc2_4_range, ldc2_4_dstep, ldc2_4_vary,  ldc2_4_defined = c_double(ldc2_4_value), c_double(ldc2_4_range), c_double(ldc2_4_dstep), c_bool(ldc2_4_vary), c_bool(ldc2_4_defined)
        velocity_scale_value, velocity_scale_range, velocity_scale_dstep, velocity_scale_vary,  velocity_scale_defined = c_double(velocity_scale_value), c_double(velocity_scale_range), c_double(velocity_scale_dstep), c_bool(velocity_scale_vary), c_bool(velocity_scale_defined)
        beam_factor1_value, beam_factor1_range, beam_factor1_dstep, beam_factor1_vary,  beam_factor1_defined = c_double(beam_factor1_value), c_double(beam_factor1_range), c_double(beam_factor1_dstep), c_bool(beam_factor1_vary), c_bool(beam_factor1_defined)
        beam_factor2_value, beam_factor2_range, beam_factor2_dstep, beam_factor2_vary,  beam_factor2_defined = c_double(beam_factor2_value), c_double(beam_factor2_range), c_double(beam_factor2_dstep), c_bool(beam_factor2_vary), c_bool(beam_factor2_defined)
        #### General
        t0_value, t0_range, t0_dstep, t0_vary,  t0_defined = c_double(t0_value), c_double(t0_range), c_double(t0_dstep), c_bool(t0_vary), c_bool(t0_defined)
        period_value, period_range, period_dstep, period_vary,  period_defined = c_double(period_value), c_double(period_range), c_double(period_dstep), c_bool(period_vary), c_bool(period_defined)
        pdot_value, pdot_range, pdot_dstep, pdot_vary,  pdot_defined = c_double(pdot_value), c_double(pdot_range), c_double(pdot_dstep), c_bool(pdot_vary), c_bool(pdot_defined)
        deltat_value, deltat_range, deltat_dstep, deltat_vary,  deltat_defined = c_double(deltat_value), c_double(deltat_range), c_double(deltat_dstep), c_bool(deltat_vary), c_bool(deltat_defined)
        gravity_dark1_value, gravity_dark1_range, gravity_dark1_dstep, gravity_dark1_vary,  gravity_dark1_defined = c_double(gravity_dark1_value), c_double(gravity_dark1_range), c_double(gravity_dark1_dstep), c_bool(gravity_dark1_vary), c_bool(gravity_dark1_defined)
        gravity_dark2_value, gravity_dark2_range, gravity_dark2_dstep, gravity_dark2_vary,  gravity_dark2_defined = c_double(gravity_dark2_value), c_double(gravity_dark2_range), c_double(gravity_dark2_dstep), c_bool(gravity_dark2_vary), c_bool(gravity_dark2_defined)
        absorb_value, absorb_range, absorb_dstep, absorb_vary,  absorb_defined = c_double(absorb_value), c_double(absorb_range), c_double(absorb_dstep), c_bool(absorb_vary), c_bool(absorb_defined)
        slope_value, slope_range, slope_dstep, slope_vary,  slope_defined = c_double(slope_value), c_double(slope_range), c_double(slope_dstep), c_bool(slope_vary), c_bool(slope_defined)
        quad_value, quad_range, quad_dstep, quad_vary,  quad_defined = c_double(quad_value), c_double(quad_range), c_double(quad_dstep), c_bool(quad_vary), c_bool(quad_defined)
        cube_value, cube_range, cube_dstep, cube_vary,  cube_defined = c_double(cube_value), c_double(cube_range), c_double(cube_dstep), c_bool(cube_vary), c_bool(cube_defined)
        third_value, third_range, third_dstep, third_vary,  third_defined = c_double(third_value), c_double(third_range), c_double(third_dstep), c_bool(third_vary), c_bool(third_defined)
        #### star spots
        stsp11_long_value, stsp11_long_range, stsp11_long_dstep, stsp11_long_vary,  stsp11_long_defined = c_double(stsp11_long_value), c_double(stsp11_long_range), c_double(stsp11_long_dstep), c_bool(stsp11_long_vary), c_bool(stsp11_long_defined)
        stsp11_lat_value, stsp11_lat_range, stsp11_lat_dstep, stsp11_lat_vary,  stsp11_lat_defined = c_double(stsp11_lat_value), c_double(stsp11_lat_range), c_double(stsp11_lat_dstep), c_bool(stsp11_lat_vary), c_bool(stsp11_lat_defined)
        stsp11_fwhm_value, stsp11_fwhm_range, stsp11_fwhm_dstep, stsp11_fwhm_vary,  stsp11_fwhm_defined = c_double(stsp11_fwhm_value), c_double(stsp11_fwhm_range), c_double(stsp11_fwhm_dstep), c_bool(stsp11_fwhm_vary), c_bool(stsp11_fwhm_defined)
        stsp11_tcen_value, stsp11_tcen_range, stsp11_tcen_dstep, stsp11_tcen_vary,  stsp11_tcen_defined = c_double(stsp11_tcen_value), c_double(stsp11_tcen_range), c_double(stsp11_tcen_dstep), c_bool(stsp11_tcen_vary), c_bool(stsp11_tcen_defined)
        stsp21_long_value, stsp21_long_range, stsp21_long_dstep, stsp21_long_vary,  stsp21_long_defined = c_double(stsp21_long_value), c_double(stsp21_long_range), c_double(stsp21_long_dstep), c_bool(stsp21_long_vary), c_bool(stsp21_long_defined)
        stsp21_lat_value, stsp21_lat_range, stsp21_lat_dstep, stsp21_lat_vary,  stsp21_lat_defined = c_double(stsp21_lat_value), c_double(stsp21_lat_range), c_double(stsp21_lat_dstep), c_bool(stsp21_lat_vary), c_bool(stsp21_lat_defined)
        stsp21_fwhm_value, stsp21_fwhm_range, stsp21_fwhm_dstep, stsp21_fwhm_vary,  stsp21_fwhm_defined = c_double(stsp21_fwhm_value), c_double(stsp21_fwhm_range), c_double(stsp21_fwhm_dstep), c_bool(stsp21_fwhm_vary), c_bool(stsp21_fwhm_defined)
        stsp21_tcen_value, stsp21_tcen_range, stsp21_tcen_dstep, stsp21_tcen_vary,  stsp21_tcen_defined = c_double(stsp21_tcen_value), c_double(stsp21_tcen_range), c_double(stsp21_tcen_dstep), c_bool(stsp21_tcen_vary), c_bool(stsp21_tcen_defined)
        #### disc
        rdisc1_value, rdisc1_range, rdisc1_dstep, rdisc1_vary,  rdisc1_defined = c_double(rdisc1_value), c_double(rdisc1_range), c_double(rdisc1_dstep), c_bool(rdisc1_vary), c_bool(rdisc1_defined)
        rdisc2_value, rdisc2_range, rdisc2_dstep, rdisc2_vary,  rdisc2_defined = c_double(rdisc2_value), c_double(rdisc2_range), c_double(rdisc2_dstep), c_bool(rdisc2_vary), c_bool(rdisc2_defined)
        height_disc_value, height_disc_range, height_disc_dstep, height_disc_vary,  height_disc_defined = c_double(height_disc_value), c_double(height_disc_range), c_double(height_disc_dstep), c_bool(height_disc_vary), c_bool(height_disc_defined)
        beta_disc_value, beta_disc_range, beta_disc_dstep, beta_disc_vary,  beta_disc_defined = c_double(beta_disc_value), c_double(beta_disc_range), c_double(beta_disc_dstep), c_bool(beta_disc_vary), c_bool(beta_disc_defined)
        temp_disc_value, temp_disc_range, temp_disc_dstep, temp_disc_vary,  temp_disc_defined = c_double(temp_disc_value), c_double(temp_disc_range), c_double(temp_disc_dstep), c_bool(temp_disc_vary), c_bool(temp_disc_defined)
        texp_disc_value, texp_disc_range, texp_disc_dstep, texp_disc_vary,  texp_disc_defined = c_double(texp_disc_value), c_double(texp_disc_range), c_double(texp_disc_dstep), c_bool(texp_disc_vary), c_bool(texp_disc_defined)
        lin_limb_disc_value, lin_limb_disc_range, lin_limb_disc_dstep, lin_limb_disc_vary,  lin_limb_disc_defined = c_double(lin_limb_disc_value), c_double(lin_limb_disc_range), c_double(lin_limb_disc_dstep), c_bool(lin_limb_disc_vary), c_bool(lin_limb_disc_defined)
        quad_limb_disc_value, quad_limb_disc_range, quad_limb_disc_dstep, quad_limb_disc_vary,  quad_limb_disc_defined = c_double(quad_limb_disc_value), c_double(quad_limb_disc_range), c_double(quad_limb_disc_dstep), c_bool(quad_limb_disc_vary), c_bool(quad_limb_disc_defined)
        temp_edge_value, temp_edge_range, temp_edge_dstep, temp_edge_vary,  temp_edge_defined = c_double(temp_edge_value), c_double(temp_edge_range), c_double(temp_edge_dstep), c_bool(temp_edge_vary), c_bool(temp_edge_defined)
        absorb_edge_value, absorb_edge_range, absorb_edge_dstep, absorb_edge_vary,  absorb_edge_defined = c_double(absorb_edge_value), c_double(absorb_edge_range), c_double(absorb_edge_dstep), c_bool(absorb_edge_vary), c_bool(absorb_edge_defined)
        #### Bright-spot
        radius_spot_value, radius_spot_range, radius_spot_dstep, radius_spot_vary,  radius_spot_defined = c_double(radius_spot_value), c_double(radius_spot_range), c_double(radius_spot_dstep), c_bool(radius_spot_vary), c_bool(radius_spot_defined)
        length_spot_value, length_spot_range, length_spot_dstep, length_spot_vary,  length_spot_defined = c_double(length_spot_value), c_double(length_spot_range), c_double(length_spot_dstep), c_bool(length_spot_vary), c_bool(length_spot_defined)
        height_spot_value, height_spot_range, height_spot_dstep, height_spot_vary,  height_spot_defined = c_double(height_spot_value), c_double(height_spot_range), c_double(height_spot_dstep), c_bool(height_spot_vary), c_bool(height_spot_defined)
        expon_spot_value, expon_spot_range, expon_spot_dstep, expon_spot_vary,  expon_spot_defined = c_double(expon_spot_value), c_double(expon_spot_range), c_double(expon_spot_dstep), c_bool(expon_spot_vary), c_bool(expon_spot_defined)
        epow_spot_value, epow_spot_range, epow_spot_dstep, epow_spot_vary,  epow_spot_defined = c_double(epow_spot_value), c_double(epow_spot_range), c_double(epow_spot_dstep), c_bool(epow_spot_vary), c_bool(epow_spot_defined)
        angle_spot_value, angle_spot_range, angle_spot_dstep, angle_spot_vary,  angle_spot_defined = c_double(angle_spot_value), c_double(angle_spot_range), c_double(angle_spot_dstep), c_bool(angle_spot_vary), c_bool(angle_spot_defined)
        yaw_spot_value, yaw_spot_range, yaw_spot_dstep, yaw_spot_vary,  yaw_spot_defined = c_double(yaw_spot_value), c_double(yaw_spot_range), c_double(yaw_spot_dstep), c_bool(yaw_spot_vary), c_bool(yaw_spot_defined)
        temp_spot_value, temp_spot_range, temp_spot_dstep, temp_spot_vary,  temp_spot_defined = c_double(temp_spot_value), c_double(temp_spot_range), c_double(temp_spot_dstep), c_bool(temp_spot_vary), c_bool(temp_spot_defined)
        tilt_spot_value, tilt_spot_range, tilt_spot_dstep, tilt_spot_vary,  tilt_spot_defined = c_double(tilt_spot_value), c_double(tilt_spot_range), c_double(tilt_spot_dstep), c_bool(tilt_spot_vary), c_bool(tilt_spot_defined)
        cfrac_spot_value, cfrac_spot_range, cfrac_spot_dstep, cfrac_spot_vary,  cfrac_spot_defined = c_double(cfrac_spot_value), c_double(cfrac_spot_range), c_double(cfrac_spot_dstep), c_bool(cfrac_spot_vary), c_bool(cfrac_spot_defined)
        #### Computational parameters
        delta_phase, nlat1f, nlat2f, nlat1c, nlat2c, npole = c_double(delta_phase), c_int(nlat1f), c_int(nlat2f), c_int(nlat1c), c_int(nlat2c), c_bool(npole)
        nlatfill, nlngfill, lfudge, llo, lhi, phase1, phase2, nrad, wavelength = c_int(nlatfill), c_int(nlngfill), c_double(lfudge), c_double(llo), c_double(lhi), c_double(phase1), c_double(phase2), c_int(nrad), c_double(wavelength)
        roche1, roche2, eclipse1, eclipse2, glens1, use_radii = c_bool(roche1), c_bool(roche2), c_bool(eclipse1), c_bool(eclipse2), c_bool(glens1), c_bool(use_radii)
        tperiod, gdark_bolom1, gdark_bolom2, mucrit1, mucrit2 = c_double(tperiod),c_double(gdark_bolom1),c_double(gdark_bolom2),c_double(mucrit1),c_double(mucrit2)
        mirror, add_disc, opaque, add_spot, nspot, iscale, info = c_bool(mirror), c_bool(add_disc), c_bool(opaque), c_bool(add_spot), c_int(nspot), c_bool(iscale), c_bool(info),
        slimb1 = create_string_buffer(slimb1.encode(), size=len(slimb1))
        slimb2 = create_string_buffer(slimb2.encode(), size=len(slimb2))

        libpylcurve=self.libpylcurve
        libpylcurve.pylcurve(
                  times, expose, ndiv, Tsize,
                  calc, lcstar1, lcdisc,
                  lcedge, lcspot, lcstar2,
                  #### Binary and stars 
                  q_value, q_range, q_dstep, q_vary, q_defined,
                  iangle_value, iangle_range, iangle_dstep, iangle_vary, iangle_defined,
                  r1_value, r1_range, r1_dstep, r1_vary, r1_defined,
                  r2_value, r2_range, r2_dstep, r2_vary, r2_defined,
                  cphi3_value, cphi3_range, cphi3_dstep, cphi3_vary, cphi3_defined,
                  cphi4_value, cphi4_range, cphi4_dstep, cphi4_vary, cphi4_defined,
                  spin1_value, spin1_range, spin1_dstep, spin1_vary, spin1_defined,
                  spin2_value, spin2_range, spin2_dstep, spin2_vary, spin2_defined,
                   teff1_value, teff1_range, teff1_dstep, teff1_vary, teff1_defined,
                  teff2_value, teff2_range, teff2_dstep, teff2_vary, teff2_defined,
                  ldc1_1_value, ldc1_1_range, ldc1_1_dstep, ldc1_1_vary, ldc1_1_defined,
                  ldc1_2_value, ldc1_2_range, ldc1_2_dstep, ldc1_2_vary, ldc1_2_defined,
                  ldc1_3_value, ldc1_3_range, ldc1_3_dstep, ldc1_3_vary, ldc1_3_defined,
                  ldc1_4_value, ldc1_4_range, ldc1_4_dstep, ldc1_4_vary, ldc1_4_defined,
                  ldc2_1_value, ldc2_1_range, ldc2_1_dstep, ldc2_1_vary, ldc2_1_defined,
                  ldc2_2_value, ldc2_2_range, ldc2_2_dstep, ldc2_2_vary, ldc2_2_defined,
                  ldc2_3_value, ldc2_3_range, ldc2_3_dstep, ldc2_3_vary, ldc2_3_defined,
                  ldc2_4_value, ldc2_4_range, ldc2_4_dstep, ldc2_4_vary, ldc2_4_defined,
                  velocity_scale_value, velocity_scale_range, velocity_scale_dstep, velocity_scale_vary, velocity_scale_defined,
                  beam_factor1_value, beam_factor1_range, beam_factor1_dstep, beam_factor1_vary, beam_factor1_defined,
                  beam_factor2_value, beam_factor2_range, beam_factor2_dstep, beam_factor2_vary, beam_factor2_defined,
                  #### General
                  t0_value, t0_range, t0_dstep, t0_vary, t0_defined,
                  period_value, period_range, period_dstep, period_vary, period_defined,
                  pdot_value, pdot_range, pdot_dstep, pdot_vary, pdot_defined,
                  deltat_value, deltat_range, deltat_dstep, deltat_vary, deltat_defined,
                  gravity_dark1_value, gravity_dark1_range, gravity_dark1_dstep, gravity_dark1_vary, gravity_dark1_defined,
                  gravity_dark2_value, gravity_dark2_range, gravity_dark2_dstep, gravity_dark2_vary, gravity_dark2_defined,
                  absorb_value, absorb_range, absorb_dstep, absorb_vary, absorb_defined,
                  slope_value, slope_range, slope_dstep, slope_vary, slope_defined,
                  quad_value, quad_range, quad_dstep, quad_vary, quad_defined,
                  cube_value, cube_range, cube_dstep, cube_vary, cube_defined,
                  third_value, third_range, third_dstep, third_vary, third_defined,
                  ####  Star spots
                  stsp11_long_value, stsp11_long_range, stsp11_long_dstep, stsp11_long_vary, stsp11_long_defined,
                  stsp11_lat_value, stsp11_lat_range, stsp11_lat_dstep, stsp11_lat_vary, stsp11_lat_defined,
                  stsp11_fwhm_value, stsp11_fwhm_range, stsp11_fwhm_dstep, stsp11_fwhm_vary, stsp11_fwhm_defined,
                  stsp11_tcen_value, stsp11_tcen_range, stsp11_tcen_dstep, stsp11_tcen_vary, stsp11_tcen_defined,
                  stsp21_long_value, stsp21_long_range, stsp21_long_dstep, stsp21_long_vary, stsp21_long_defined,
                  stsp21_lat_value, stsp21_lat_range, stsp21_lat_dstep, stsp21_lat_vary, stsp21_lat_defined,
                  stsp21_fwhm_value, stsp21_fwhm_range, stsp21_fwhm_dstep, stsp21_fwhm_vary, stsp21_fwhm_defined,
                  stsp21_tcen_value, stsp21_tcen_range, stsp21_tcen_dstep, stsp21_tcen_vary, stsp21_tcen_defined,
                  #### disc
                  rdisc1_value, rdisc1_range, rdisc1_dstep, rdisc1_vary, rdisc1_defined,
                  rdisc2_value, rdisc2_range, rdisc2_dstep, rdisc2_vary, rdisc2_defined,
                  height_disc_value, height_disc_range, height_disc_dstep, height_disc_vary, height_disc_defined,
                  beta_disc_value, beta_disc_range, beta_disc_dstep, beta_disc_vary, beta_disc_defined,
                  temp_disc_value, temp_disc_range, temp_disc_dstep, temp_disc_vary, temp_disc_defined,
                  texp_disc_value, texp_disc_range, texp_disc_dstep, texp_disc_vary, texp_disc_defined,
                  lin_limb_disc_value, lin_limb_disc_range, lin_limb_disc_dstep, lin_limb_disc_vary, lin_limb_disc_defined,
                  quad_limb_disc_value, quad_limb_disc_range, quad_limb_disc_dstep, quad_limb_disc_vary, quad_limb_disc_defined,
                  temp_edge_value, temp_edge_range, temp_edge_dstep, temp_edge_vary, temp_edge_defined,
                  absorb_edge_value, absorb_edge_range, absorb_edge_dstep, absorb_edge_vary, absorb_edge_defined,
                  #### Bright-spot
                  radius_spot_value, radius_spot_range, radius_spot_dstep, radius_spot_vary, radius_spot_defined,
                  length_spot_value, length_spot_range, length_spot_dstep, length_spot_vary, length_spot_defined,
                  height_spot_value, height_spot_range, height_spot_dstep, height_spot_vary, height_spot_defined,
                  expon_spot_value, expon_spot_range, expon_spot_dstep, expon_spot_vary, expon_spot_defined,
                  epow_spot_value, epow_spot_range, epow_spot_dstep, epow_spot_vary, epow_spot_defined,
                  angle_spot_value, angle_spot_range, angle_spot_dstep, angle_spot_vary, angle_spot_defined,
                  yaw_spot_value, yaw_spot_range, yaw_spot_dstep, yaw_spot_vary, yaw_spot_defined,
                  temp_spot_value, temp_spot_range, temp_spot_dstep, temp_spot_vary, temp_spot_defined,
                  tilt_spot_value, tilt_spot_range, tilt_spot_dstep, tilt_spot_vary, tilt_spot_defined,
                  cfrac_spot_value, cfrac_spot_range, cfrac_spot_dstep, cfrac_spot_vary, cfrac_spot_defined,
                  ####  Computational parameters
                  delta_phase, nlat1f, nlat2f, nlat1c, nlat2c, npole,
                  nlatfill, nlngfill, lfudge, llo, lhi, phase1, phase2, nrad, wavelength,
                  roche1, roche2, eclipse1, eclipse2, glens1, use_radii,
                  tperiod, gdark_bolom1, gdark_bolom2, mucrit1, mucrit2,
                  slimb1, slimb2, mirror, add_disc, opaque, add_spot, nspot, iscale, info
                            )
        self.libpylcurve  = libpylcurve
        print('ok')

    def lc_from_smodel(self, smodel, times, expose=0, ndiv=1, info=True):
        '''
        parameters:
        -----------------------------------------------------------------------
        smodel [str] --- the name of modle file
        times [float array 1D] --- it must be 1D np.array
        wdwarf [float] --- White dwarf's contribution
        logg1 [float] --- flux-weighted logg of star1
        logg2 [float] --- flux-weighted logg of star2
        rv1: [float] --- volume-averaged radius of star1
        rv2: [float] --- volume-averaged radius of star2
        expose [float array 1D] --- The exposure length in the same units as the time
        ndiv [int or int array 1D] --- Factor to split up data points to allow for finite exposures
        info [bool] --- if true, it prints out array sizes to stderr
        '''
        Tsize = len(times)
        ####--------------inintalize time and light curves arrays-----------------------------------------
        if isinstance(expose, float): expose = expose*np.ones(Tsize, dtype=np.double)
        if isinstance(ndiv, float): ndiv = ndiv*np.ones(Tsize, dtype=np.int)
        calc, lcstar1, lcdisc, lcedge, lcspot, lcstar2 = np.empty((6, Tsize), dtype=np.float)
        ####----------------------- declare variables------------------------------------------------------
        smodel = create_string_buffer(smodel.encode(), size=len(smodel))
        times = times.ctypes.data_as(POINTER(c_double*Tsize))
        expose = expose.ctypes.data_as(POINTER(c_double*Tsize))
        ndiv = ndiv.ctypes.data_as(POINTER(c_int*Tsize))
        calc = calc.ctypes.data_as(POINTER(c_double*Tsize))
        lcstar1 = lcstar1.ctypes.data_as(POINTER(c_double*Tsize))
        lcdisc = lcdisc.ctypes.data_as(POINTER(c_double*Tsize))
        lcedge = lcedge.ctypes.data_as(POINTER(c_double*Tsize))
        lcspot = lcspot.ctypes.data_as(POINTER(c_double*Tsize))
        lcstar2 = lcstar2.ctypes.data_as(POINTER(c_double*Tsize))
        #wdwarf = c_double(wdwarf)
        #logg1 = c_double(logg1)
        #logg2 = c_double(logg2)
        #rv1 = c_double(rv1)
        #rv2 = c_double(rv2)
        info = c_bool(info)
        libpylcurve=self.libpylcurve
        libpylcurve.pylcurve_smodel(smodel, 
                      times, expose, ndiv, Tsize,
                      info,
                      calc, lcstar1, lcdisc,
                      lcedge, lcspot, lcstar2)
        print('ok')
