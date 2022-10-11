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
time = np.array([0,1], dtype=np.float)
expose = np.array([0,0], dtype=np.float)
ndiv = np.array([0,0], dtype=np.float)


llcurve = lcurve()
llcurve.lc(time, expose=expose, ndiv=ndiv, info=True)


