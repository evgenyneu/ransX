# ----- Parameter file for rans(eXtreme) and CCP project ---------- #
[]
## Input Datadir ........................................... ## [prop,eht_data,DATA_D/TEVOL/]
## Data File List .......................................... ## [prop,eht_res,tseries_ccptwo_128x128x128_cosma_120secs_nb_evol.npy,tseries_ccptwo_256x256x256_cosma_120secs_nb_evol.npy,tseries_ccptwo_512x512x512_cosma_120secs_nb_evol.npy]
## Filename Prefix For Plots ............................... ## [prop,prefix,ccptwo_resEvol_]
## Geometry; ig = 1 Cartesian, ig = 2 Spherical ............ ## [prop,ig,1]
## Equation Of State; ieos = 1 Ideal Gas, ieos = 3 HelmEos . ## [prop,ieos,1]
## Limit Axis .............................................. ## [prop,laxis,2]
## X-axis Left boundary for properties ..................... ## [prop,xbl,4.04e8]
## X-axis Right boundary for properties .................... ## [prop,xbr,1.18e9]
[]
## Turbulent Kinetic Energy Evolution ...................... ## [tkeevol,True,1.,550.,8.e46,1.e46,0]
## Mach Number Max Evolution ............................... ## [machmxevol,False,1.,800.,6.e-2,1.e-2,0]
## Mach Number Mean Evolution .............................. ## [machmeevol,False,1.,800.,4.5e-2,1.e-2,0]
## Convection Boundaries Position Evolution ................ ## [cnvzbndry,True,1.,550.,0.96e9,0.84e9,2]
## Energy Source Term Evolution ............................ ## [enesource,False,1.,800.,5.e45,4.e45,0]
## Convective RMS Velocity Evolution ....................... ## [convelrms,False,1.,800.,2.2e7,1.e7,0]
## Convective Turnover Timescale Evolution ................. ## [convturn,False,1.,800.,100.,50.,0]
## Residual Max Continuity Equation Evolution .............. ## [contresmax,False,1.,800.,2.e1,0.,0]
## Residual Mean Continuity Equation Evolution ............. ## [contresmean,False,1.,800.,5.e0,0.,0]
## Residual Max Total Energy Equation Evolution ............ ## [teeresmax,False,1.,800.,8.e18,0.,0]
## Residual Mean Total Energy Equation Evolution ........... ## [teeresmean,False,1.,800.,2.e18,0.,0]
## X0002 Evolution (CCP project) ........................... ## [x0002evol,False,1.,2000.,2.2e-1,0.,2]