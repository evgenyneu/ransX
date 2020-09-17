# ----- Parameter file for rans(eXtreme) and CCP-TWO-LAYERS ---------- #
[]
## Input Data Folder ....................................... ## [prop,eht_data,DATA_D/TSERIES/]
## Resolution Study Input Files List ....................... ## [prop,eht_res,tseries_oburn384x192x192_trange0s-6s_tavg3s_prot.npy,tseries_oburn384x192x192_trange458s-463s_tavg3s_prot.npy,tseries_oburn384x192x192_trange758s-763s_tavg3s_prot.npy,tseries_oburn384x192x192_trange1057s-1062s_tavg3s_prot.npy]
## Project Label (oburn, ccp: for now only) ................ ## [prop,plabel,oburn]
## Filename Prefix For Plots ............................... ## [prop,prefix,oburn_xrhox_prof_evol]
## Equation Of State; ieos = 1 Ideal Gas, ieos = 3 HelmEos . ## [prop,ieos,3]
## Geometry; ig = 1 Cartesian, ig = 2 Spherical ............ ## [prop,ig,2]
## Central Time Index ...................................... ## [prop,intc,0]
## Limit Axis .............................................. ## [prop,laxis,2]
## X-axis Left boundary for properties ..................... ## [prop,xbl,4.2e8]
## X-axis Right boundary for properties .................... ## [prop,xbr,9.8e8]
## Nuclear network ......................................... ## [network,neut,prot,he4,c12,o16,ne20,na23,mg24,si28,p31,s32,s34,cl35,ar36,ar38,k39,ca40,ca42,ti44,ti46,cr48,cr50,fe52,fe54,ni56] 
[]
## Temperature stratification .............................. ## [temp,False,3.7e8,9.8e8,3.8e9,0.8e9,0]
## Brunt-Vaisalla frequency ................................ ## [nsq,False,3.7e8,9.8e8,1.5,-0.15,0]
## Turbulent Kinetic Energy Stratification ................. ## [tkie,False,3.7e8,9.8e8,2.5e14,0.,0]
## Internal Energy Flux Stratification ..................... ## [eintflx,False,3.7e8,9.8e8,0.7e28,-0.5e27,0]
## Entropy Flux Stratification ............................. ## [entrflx,False,3.7e8,9.8e8,0.1e17,-1.e17,0]
## Pressure X Flux Stratification .......................... ## [pressxflx,False,3.7e8,9.8e8,2.e26,-3.e26,0]
## Temperature Flux Stratification ......................... ## [tempflx,False,3.7e8,9.8e8,0.8e14,-1.e13,0]
## Enthalpy Flux Stratification ............................ ## [enthflx,False,3.7e8,9.8e8,1.3e28,-1.e27,0]
## Turbulent Mass Flux Stratification ...................... ## [tmsflx,False,3.7e8,9.8e8,4.e9,-3.5e10,0]
## Turbulent Radial Velocity RMS ........................... ## [uxrms,False,3.7e8,9.8e8,1.7e7,-1.e6,0]
## Turbulent Uy Velocity RMS ............................... ## [uyrms,False,3.7e8,9.8e8,1.7e7,-1.e6,0]
## Turbulent Uz Velocity RMS ............................... ## [uzrms,False,3.7e8,9.8e8,1.7e7,-1.e6,0]
## Buoyancy ................................................ ## [buoy,False,3.7e8,9.8e8,1.2e8,-0.1e8,0]
## Density Fluctuations (RMS) amplitude .................... ## [ddrms,False,3.7e8,9.8e8,3.e-1,1.e-3,0]
[]
## Neutrons X stratification ............................... ## [x_neut,True,3.7e8,9.8e8,3.e-15,1.e-22,0]
## Neutrons density stratification ......................... ## [xrho_neut,True,3.7e8,9.8e8,5.e-11,-0.2e-12,0]
## Neutrons flux X stratification .......................... ## [xflxx_neut,False,3.7e8,9.8e8,3.e10,-1.e9,0]
[]
## Protons X stratification ................................ ## [x_prot,True,3.7e8,9.8e8,1.e-9,1.e-18,0]
## Protons density stratification .......................... ## [xrho_prot,True,3.7e8,9.8e8,2.e-4,-0.2e-4,0]
## Protons flux X stratification ........................... ## [xflxx_prot,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## he4 X stratification .................................... ## [x_he4,True,3.7e8,9.8e8,1.e-8,1.e-14,0]
## he4 density stratification .............................. ## [xrho_he4,True,3.7e8,9.8e8,8.e-3,-0.2e-3,0]
## he4 flux X stratification ............................... ## [xflxx_he4,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## c12 X stratification .................................... ## [x_c12,True,3.7e8,9.8e8,1.e-3,1.e-8,0]
## c12 density stratification .............................. ## [xrho_c12,True,3.7e8,9.8e8,7.e1,-0.1e1,0]
## c12 flux X stratification ............................... ## [xflxx_c12,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## o16 X stratification .................................... ## [x_o16,True,3.7e8,9.8e8,1.e0,5.e-3,0]
## o16 density stratification .............................. ## [xrho_o16,True,3.7e8,9.8e8,8.e5,-0.2e5,0]
## o16 flux X stratification ............................... ## [xflxx_o16,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## ne20 X stratification ................................... ## [x_ne20,True,3.7e8,9.8e8,1.e0,1.e-8,0]
## ne20 density stratification ............................. ## [xrho_ne20,True,3.7e8,9.8e8,8.e4,-0.2e4,0]
## ne20 flux X stratification .............................. ## [xflxx_ne20,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## na23 X stratification ................................... ## [x_na23,True,3.7e8,9.8e8,1.e-2,1.e-12,0]
## na23 density stratification ............................. ## [xrho_na23,True,3.7e8,9.8e8,1.6e3,-0.2e3,0]
## na23 flux X stratification .............................. ## [xflxx_na23,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## mg24 X stratification ................................... ## [x_mg24,True,3.7e8,9.8e8,1.e0,1.e-6,0]
## mg24 density stratification ............................. ## [xrho_mg24,True,3.7e8,9.8e8,8.e4,-0.2e4,0]
## mg24 flux X stratification .............................. ## [xflxx_mg24,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## si28 X stratification ................................... ## [x_si28,True,3.7e8,9.8e8,1.e0,5.e-3,0]
## si28 density stratification ............................. ## [xrho_si28,True,3.7e8,9.8e8,2.5e6,-0.2e6,0]
## si28 flux X stratification .............................. ## [xflxx_si28,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## p31 X stratification .................................... ## [x_p31,True,3.7e8,9.8e8,2.e-3,2.e-4,0]
## p31 density stratification .............................. ## [xrho_p31,True,3.7e8,9.8e8,1.4e3,-0.2e3,0]
## p31 flux X stratification ............................... ## [xflxx_p31,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## s32 X stratification .................................... ## [x_s32,True,3.7e8,9.8e8,4.e-1,1.e-4,0]
## s32 density stratification .............................. ## [xrho_s32,True,3.7e8,9.8e8,1.6e6,-0.2e6,0]
## s32 flux X stratification ............................... ## [xflxx_s32,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## s34 X stratification .................................... ## [x_s34,True,3.7e8,9.8e8,1.e-1,1.e-5,0]
## s34 density stratification .............................. ## [xrho_s34,True,3.7e8,9.8e8,6.e4,-0.2e4,0]
## s34 flux X stratification ............................... ## [xflxx_s34,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## cl35 X stratification ................................... ## [x_cl35,True,3.7e8,9.8e8,1.e-3,1.e-6,0]
## cl35 density stratification ............................. ## [xrho_cl35,True,3.7e8,9.8e8,2.5e3,-0.2e3,0]
## cl35 flux X stratification .............................. ## [xflxx_cl35,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## ar36 X stratification ................................... ## [x_ar36,True,3.7e8,9.8e8,1.e-1,1.e-5,0]
## ar36 density stratification ............................. ## [xrho_ar36,True,3.7e8,9.8e8,2.e5,-0.2e5,0]
## ar36 flux X stratification .............................. ## [xflxx_ar36,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## ar38 X stratification ................................... ## [x_ar38,True,3.7e8,9.8e8,1.e-1,1.e-5,0]
## ar38 density stratification ............................. ## [xrho_ar38,True,3.7e8,9.8e8,1.4e5,-0.2e5,0]
## ar38 flux X stratification .............................. ## [xflxx_ar38,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## k39 X stratification .................................... ## [x_k39,True,3.7e8,9.8e8,2.e-3,1.e-6,0]
## k39 density stratification .............................. ## [xrho_k39,True,3.7e8,9.8e8,5.e3,-0.2e3,0]
## k39 flux X stratification ............................... ## [xflxx_k39,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## ca40 X stratification ................................... ## [x_ca40,True,3.7e8,9.8e8,1.e-1,1.e-5,0]
## ca40 density stratification ............................. ## [xrho_ca40,True,3.7e8,9.8e8,2.e5,-0.2e5,0]
## ca40 flux X stratification .............................. ## [xflxx_ca40,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## ca42 X stratification ................................... ## [x_ca42,True,3.7e8,9.8e8,6.e-4,8.e-6,0]
## ca42 density stratification ............................. ## [xrho_ca42,True,3.7e8,9.8e8,3.e3,-0.2e3,0]
## ca42 flux X stratification .............................. ## [xflxx_ca42,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## ti44 X stratification ................................... ## [x_ti44,True,3.7e8,9.8e8,1.e-5,1.e-10,0]
## ti44 density stratification ............................. ## [xrho_ti44,True,3.7e8,9.8e8,1.6e1,-0.1e1,0]
## ti44 flux X stratification .............................. ## [xflxx_ti44,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## ti46 X stratification ................................... ## [x_ti46,True,3.7e8,9.8e8,1.e-3,1.e-6,0]
## ti46 density stratification ............................. ## [xrho_ti46,True,3.7e8,9.8e8,3.e3,-0.2e3,0]
## ti46 flux X stratification .............................. ## [xflxx_ti46,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## cr48 X stratification ................................... ## [x_cr48,True,3.7e8,9.8e8,1.e-6,1.e-18,0]
## cr48 density stratification ............................. ## [xrho_cr48,True,3.7e8,9.8e8,1.75e0,-0.2e0,0]
## cr48 flux X stratification .............................. ## [xflxx_cr48,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## cr50 X stratification ................................... ## [x_cr50,True,3.7e8,9.8e8,1.e-3,1.e-9,0]
## cr50 density stratification ............................. ## [xrho_cr50,True,3.7e8,9.8e8,1.2e3,-0.2e3,0]
## cr50 flux X stratification .............................. ## [xflxx_cr50,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## fe52 X stratification ................................... ## [x_fe52,True,3.7e8,9.8e8,1.e-7,1.e-20,0]
## fe52 density stratification ............................. ## [xrho_fe52,True,3.7e8,9.8e8,6.e-2,-0.2e-2,0]
## fe52 flux X stratification .............................. ## [xflxx_fe52,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## fe54 X stratification ................................... ## [x_fe54,True,3.7e8,9.8e8,1.e-4,1.e-8,0]
## fe54 density stratification ............................. ## [xrho_fe54,True,3.7e8,9.8e8,1.8e2,-0.2e2,0]
## fe54 flux X stratification .............................. ## [xflxx_fe54,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]
[]
## ni56 X stratification ................................... ## [x_ni56,True,3.7e8,9.8e8,1.e-9,1.e-17,0]
## ni56 density stratification ............................. ## [xrho_ni56,True,3.7e8,9.8e8,1.2e-3,-0.1e-3,0]
## ni56 flux X stratification .............................. ## [xflxx_ni56,False,3.7e8,9.8e8,1.5e1,-1.5e1,0]