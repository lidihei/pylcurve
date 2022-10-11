import numpy as np
import os
from pylcurve.lightcurve import lcurve
import ctypes
lib = ctypes.CDLL('../pylcurve/lib/libpylcurve.so')


argurs = '''times, expose, ndiv, q_value, q_range, q_dstep, q_vary, q_defined, iangle_value, 
iangle_range, iangle_dstep, iangle_vary, iangle_defined, r1_value, r1_range, r1_dstep, r1_vary, r1_defined, r2_value, r2_range, r2_dstep, r2_vary, r2_defined, cphi3_value, cphi3_ran
ge, cphi3_dstep, cphi3_vary, cphi3_defined, cphi4_value, cphi4_range, cphi4_dstep, cphi4_vary, cphi4_defined, spin1_value, spin1_range, spin1_dstep, spin1_vary, spin1_defined, spin2
_value, spin2_range, spin2_dstep, spin2_vary, spin2_defined, teff1_value, teff1_range, teff1_dstep, teff1_vary, teff1_defined, teff2_value, teff2_range, teff2_dstep, teff2_vary, tef
f2_defined, ldc1_1_value, ldc1_1_range, ldc1_1_dstep, ldc1_1_vary, ldc1_1_defined, ldc1_2_value, ldc1_2_range, ldc1_2_dstep, ldc1_2_vary, ldc1_2_defined, ldc1_3_value, ldc1_3_range,
 ldc1_3_dstep, ldc1_3_vary, ldc1_3_defined, ldc1_4_value, ldc1_4_range, ldc1_4_dstep, ldc1_4_vary, ldc1_4_defined, ldc2_1_value, ldc2_1_range, ldc2_1_dstep, ldc2_1_vary, ldc2_1_defi
ned, ldc2_2_value, ldc2_2_range, ldc2_2_dstep, ldc2_2_vary, ldc2_2_defined, ldc2_3_value, ldc2_3_range, ldc2_3_dstep, ldc2_3_vary, ldc2_3_defined, ldc2_4_value, ldc2_4_range, ldc2_4
_dstep, ldc2_4_vary, ldc2_4_defined, velocity_scale_value, velocity_scale_range, velocity_scale_dstep, velocity_scale_vary, velocity_scale_defined, beam_factor1_value, beam_factor1_
range, beam_factor1_dstep, beam_factor1_vary, beam_factor1_defined, beam_factor2_value, beam_factor2_range, beam_factor2_dstep, beam_factor2_vary, beam_factor2_defined, t0_value, t0
_range, t0_dstep, t0_vary, t0_defined, period_value, period_range, period_dstep, period_vary, period_defined, pdot_value, pdot_range, pdot_dstep, pdot_vary, pdot_defined, deltat_val
ue, deltat_range, deltat_dstep, deltat_vary, deltat_defined, gravity_dark1_value, gravity_dark1_range, gravity_dark1_dstep, gravity_dark1_vary, gravity_dark1_defined, gravity_dark2_
value, gravity_dark2_range, gravity_dark2_dstep, gravity_dark2_vary, gravity_dark2_defined, absorb_value, absorb_range, absorb_dstep, absorb_vary, absorb_defined, slope_value, slope
_range, slope_dstep, slope_vary, slope_defined, quad_value, quad_range, quad_dstep, quad_vary, quad_defined, cube_value, cube_range, cube_dstep, cube_vary, cube_defined, third_value
, third_range, third_dstep, third_vary, third_defined, stsp11_long_value, stsp11_long_range, stsp11_long_dstep, stsp11_long_vary, stsp11_long_defined, stsp11_lat_value, stsp11_lat_r
ange, stsp11_lat_dstep, stsp11_lat_vary, stsp11_lat_defined, stsp11_fwhm_value, stsp11_fwhm_range, stsp11_fwhm_dstep, stsp11_fwhm_vary, stsp11_fwhm_defined, stsp11_tcen_value, stsp1
1_tcen_range, stsp11_tcen_dstep, stsp11_tcen_vary, stsp11_tcen_defined, stsp21_long_value, stsp21_long_range, stsp21_long_dstep, stsp21_long_vary, stsp21_long_defined, stsp21_lat_va
lue, stsp21_lat_range, stsp21_lat_dstep, stsp21_lat_vary, stsp21_lat_defined, stsp21_fwhm_value, stsp21_fwhm_range, stsp21_fwhm_dstep, stsp21_fwhm_vary, stsp21_fwhm_defined, stsp21_
tcen_value, stsp21_tcen_range, stsp21_tcen_dstep, stsp21_tcen_vary, stsp21_tcen_defined, rdisc1_value, rdisc1_range, rdisc1_dstep, rdisc1_vary, rdisc1_defined, rdisc2_value, rdisc2_
range, rdisc2_dstep, rdisc2_vary, rdisc2_defined, height_disc_value, height_disc_range, height_disc_dstep, height_disc_vary, height_disc_defined, beta_disc_value, beta_disc_range, b
eta_disc_dstep, beta_disc_vary, beta_disc_defined, temp_disc_value, temp_disc_range, temp_disc_dstep, temp_disc_vary, temp_disc_defined, texp_disc_value, texp_disc_range, texp_disc_
dstep, texp_disc_vary, texp_disc_defined, lin_limb_disc_value, lin_limb_disc_range, lin_limb_disc_dstep, lin_limb_disc_vary, lin_limb_disc_defined, quad_limb_disc_value, quad_limb_d
isc_range, quad_limb_disc_dstep, quad_limb_disc_vary, quad_limb_disc_defined, temp_edge_value, temp_edge_range, temp_edge_dstep, temp_edge_vary, temp_edge_defined, absorb_edge_value
, absorb_edge_range, absorb_edge_dstep, absorb_edge_vary, absorb_edge_defined, radius_spot_value, radius_spot_range, radius_spot_dstep, radius_spot_vary, radius_spot_defined, length
_spot_value, length_spot_range, length_spot_dstep, length_spot_vary, length_spot_defined, height_spot_value, height_spot_range, height_spot_dstep, height_spot_vary, height_spot_defi
ned, expon_spot_value, expon_spot_range, expon_spot_dstep, expon_spot_vary, expon_spot_defined, epow_spot_value, epow_spot_range, epow_spot_dstep, epow_spot_vary, epow_spot_defined,
 angle_spot_value, angle_spot_range, angle_spot_dstep, angle_spot_vary, angle_spot_defined, yaw_spot_value, yaw_spot_range, yaw_spot_dstep, yaw_spot_vary, yaw_spot_defined, temp_spo
t_value, temp_spot_range, temp_spot_dstep, temp_spot_vary, temp_spot_defined, tilt_spot_value, tilt_spot_range, tilt_spot_dstep, tilt_spot_vary, tilt_spot_defined, cfrac_spot_value,
 cfrac_spot_range, cfrac_spot_dstep, cfrac_spot_vary, cfrac_spot_defined, delta_phase, nlat1f, nlat2f, nlat1c, nlat2c, npole, nlatfill, nlngfill, lfudge, llo, lhi, phase1, phase2, n
rad, wavelength, roche1, roche2, eclipse1, eclipse2, glens1, use_radii, tperiod, gdark_bolom1, gdark_bolom2, mucrit1, mucrit2, slimb1, slimb2, mirror, add_disc, opaque, add_spot, ns
pot, iscale, info'''

argurs =  argurs.replace('\n', '').split(',')
times = np.array([0,1], dtype=np.float)
expose = np.array([0,0], dtype=np.float)
ndiv = np.array([0,0], dtype=np.float)


llcurve = lcurve()
llcurve.lc(times, expose=expose, ndiv=ndiv,
       ###Binary and stars
       q_value = 0.9670,  q_range = 0.,  q_dstep = 0.,  q_vary = False,  q_defined = True,
       iangle_value = 86.5063,  iangle_range = 0.,  iangle_dstep = 0.,  iangle_vary = False,  iangle_defined = True,
       r1_value = 0.006292,  r1_range = 0.,  r1_dstep = 0.,  r1_vary = False,  r1_defined = True,
       r2_value = 0.097168,  r2_range = 0.,  r2_dstep = 0.,  r2_vary = False,  r2_defined = True,
       cphi3_value = 0.015,  cphi3_range = 0.,  cphi3_dstep = 0.,  cphi3_vary = False,  cphi3_defined = True,
       cphi4_value = 0.017,  cphi4_range = 0.,  cphi4_dstep = 0.,  cphi4_vary = False,  cphi4_defined = True,
       spin1_value = 1.,  spin1_range = 0.,  spin1_dstep = 0.,  spin1_vary = False,  spin1_defined = True,
       spin2_value = 1.,  spin2_range = 0.,  spin2_dstep = 0.,  spin2_vary = False,  spin2_defined = True,
       teff1_value = 15918.02,  teff1_range = 0.,  teff1_dstep = 0.,  teff1_vary = False,  teff1_defined = True,
       teff2_value =  34570.39,  teff2_range = 0.,  teff2_dstep = 0.,  teff2_vary = False,  teff2_defined = True,
       ldc1_1_value = 0.81760,  ldc1_1_range = 0.,  ldc1_1_dstep = 0.,  ldc1_1_vary = False,  ldc1_1_defined = True,
       ldc1_2_value = -0.6685,  ldc1_2_range = 0.,  ldc1_2_dstep = 0.,  ldc1_2_vary = False,  ldc1_2_defined = True,
       ldc1_3_value = 0.6119,  ldc1_3_range = 0.,  ldc1_3_dstep = 0.,  ldc1_3_vary = False,  ldc1_3_defined = True,
       ldc1_4_value = -0.2362,  ldc1_4_range = 0.,  ldc1_4_dstep = 0.,  ldc1_4_vary = False,  ldc1_4_defined = True,
       ldc2_1_value = 0.8177,  ldc2_1_range = 0.,  ldc2_1_dstep = 0.,  ldc2_1_vary = False,  ldc2_1_defined = True,
       ldc2_2_value = -0.9078,  ldc2_2_range = 0.,  ldc2_2_dstep = 0.,  ldc2_2_vary = False,  ldc2_2_defined = True,
       ldc2_3_value = 0.7550,  ldc2_3_range = 0.,  ldc2_3_dstep = 0.,  ldc2_3_vary = False,  ldc2_3_defined = True,
       ldc2_4_value = -0.2518,  ldc2_4_range = 0.,  ldc2_4_dstep = 0.,  ldc2_4_vary = False,  ldc2_4_defined = True,
       velocity_scale_value = 323.4547,  velocity_scale_range = 1.,  velocity_scale_dstep = 1.,  velocity_scale_vary = True,  velocity_scale_defined = True,
       beam_factor1_value = 2.,  beam_factor1_range = 0.1,  beam_factor1_dstep = 0.02,  beam_factor1_vary = False,  beam_factor1_defined = True,
       beam_factor2_value = 1.3131,  beam_factor2_range = 0.,  beam_factor2_dstep = 0.,  beam_factor2_vary = True,  beam_factor2_defined = True,
       ##//General
       t0_value = 1.2012e-5,  t0_range = 0.,  t0_dstep = 0.,  t0_vary = False,  t0_defined = True,
       period_value = 1.,  period_range = 0.,  period_dstep = 0.,  period_vary = False,  period_defined = True,
       pdot_value = 0.,  pdot_range = 0.,  pdot_dstep = 0.,  pdot_vary = False,  pdot_defined = False,
       deltat_value = 0.,  deltat_range = 0.,  deltat_dstep = 0.,  deltat_vary = False,  deltat_defined = True,
       gravity_dark1_value = 0.44796,  gravity_dark1_range = 0.,  gravity_dark1_dstep = 0.,  gravity_dark1_vary = False,  gravity_dark1_defined = True,
       gravity_dark2_value = 0.44796,  gravity_dark2_range = 0.,  gravity_dark2_dstep = 0.,  gravity_dark2_vary = False,  gravity_dark2_defined = True,
       absorb_value = 1.,  absorb_range = 0.,  absorb_dstep = 0.,  absorb_vary = False,  absorb_defined = True,
       slope_value = 0.,  slope_range = 0.,  slope_dstep = 0.,  slope_vary = False,  slope_defined = True,
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
       rdisc1_value = 0.05,  rdisc1_range = 0.,  rdisc1_dstep = 0.,  rdisc1_vary = False,  rdisc1_defined = True,
       rdisc2_value = 0.35,  rdisc2_range = 0.,  rdisc2_dstep = 0.,  rdisc2_vary = False,  rdisc2_defined = True,
       height_disc_value = 0.1,  height_disc_range = 0.,  height_disc_dstep = 0.,  height_disc_vary = False,  height_disc_defined = True,
       beta_disc_value = 1.5,  beta_disc_range = 0.,  beta_disc_dstep = 0.,  beta_disc_vary = False,  beta_disc_defined = True,
       temp_disc_value = 3000.,  temp_disc_range = 0.,  temp_disc_dstep = 0.,  temp_disc_vary = False,  temp_disc_defined = True,
       texp_disc_value = -1.8,  texp_disc_range = 0.,  texp_disc_dstep = 0.,  texp_disc_vary = False,  texp_disc_defined = True,
       lin_limb_disc_value = 0.3,  lin_limb_disc_range = 0.,  lin_limb_disc_dstep = 0.,  lin_limb_disc_vary = False,  lin_limb_disc_defined = True,
       quad_limb_disc_value = 0.,  quad_limb_disc_range = 0.,  quad_limb_disc_dstep = 0.,  quad_limb_disc_vary = False,  quad_limb_disc_defined = True,
       temp_edge_value = 0.,  temp_edge_range = 0.,  temp_edge_dstep = 0.,  temp_edge_vary = False,  temp_edge_defined = False,
       absorb_edge_value = 0.,  absorb_edge_range = 0.,  absorb_edge_dstep = 0.,  absorb_edge_vary = False,  absorb_edge_defined = False,
       ##//Bright-spot
       radius_spot_value = 0.35,  radius_spot_range = 0.,  radius_spot_dstep = 0.,  radius_spot_vary = False,  radius_spot_defined = True,
       length_spot_value = 0.02,  length_spot_range = 0.,  length_spot_dstep = 0.,  length_spot_vary = False,  length_spot_defined = True,
       height_spot_value = 0.05,  height_spot_range = 0.,  height_spot_dstep = 0.,  height_spot_vary = False,  height_spot_defined = True,
       expon_spot_value = 0.,  expon_spot_range = 0.,  expon_spot_dstep = 0.,  expon_spot_vary = False,  expon_spot_defined = True,
       epow_spot_value = 1.,  epow_spot_range = 0.,  epow_spot_dstep = 0.,  epow_spot_vary = False,  epow_spot_defined = True,
       angle_spot_value = 140.,  angle_spot_range = 0.,  angle_spot_dstep = 0.,  angle_spot_vary = False,  angle_spot_defined = True,
       yaw_spot_value = 0.,  yaw_spot_range = 0.,  yaw_spot_dstep = 0.,  yaw_spot_vary = False,  yaw_spot_defined = True,
       temp_spot_value = 15000.,  temp_spot_range = 0.,  temp_spot_dstep = 0.,  temp_spot_vary = False,  temp_spot_defined = True,
       tilt_spot_value = 90.,  tilt_spot_range = 0.,  tilt_spot_dstep = 0.,  tilt_spot_vary = False,  tilt_spot_defined = True,
       cfrac_spot_value = 0.2,  cfrac_spot_range = 0.,  cfrac_spot_dstep = 0.,  cfrac_spot_vary = False,  cfrac_spot_defined = True,
       ##Computational parameters
       delta_phase = 3.e-8,  nlat1f = 50,  nlat2f = 210,  nlat1c = 50,  nlat2c = 170,  npole = True,
       nlatfill = 3,  nlngfill = 2,  lfudge = 0.07,  llo = 0.,  lhi = -50.,  phase1 = 0.018,  phase2 = 0.482,  nrad = 40,  wavelength = 600.,
       roche1 = False,  roche2 = True,  eclipse1 = True,  eclipse2 = True,  glens1 = True,  use_radii=1.,
       tperiod = 0.40373,  gdark_bolom1 = 0.,  gdark_bolom2 = 0.,  mucrit1 = 0.,  mucrit2 = 0.,
       slimb1 = 'Claret', slimb2 = 'Claret',  mirror = False,  add_disc = False,  opaque = False,  add_spot = False,  nspot = 100,  iscale = False,
       info = True 
          )


