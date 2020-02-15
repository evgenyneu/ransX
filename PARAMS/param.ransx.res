# ----- Parameter file for rans(eXtreme) and CCP-TWO-LAYERS ---------- #
[]
## Input Data Folder ....................................... ## [prop,eht_data,DATA/TSERIES/]
## Resolution Study Input Files List ....................... ## [prop,eht_res,tseries_ccptwo_64c_liger_fixedmuOpt3_1500secs.npy,tseries_ccptwo_128c_liger_fixedmuOpt3_1500secs.npy,tseries_ccptwo_256c_cosma_1500secs.npy]
## Project Label (oburn, ccp: for now only) ................ ## [prop,plabel,ccp]
## Filename Prefix For Plots ............................... ## [prop,prefix,ccptwo_resStudyFieldsTavg1500s_]
## Equation Of State; ieos = 1 Ideal Gas, ieos = 3 HelmEos . ## [prop,ieos,1]
## Geometry; ig = 1 Cartesian, ig = 2 Spherical ............ ## [prop,ig,1]
## Central Time Index ...................................... ## [prop,intc,265]
## Limit Axis .............................................. ## [prop,laxis,2]
## X-axis Left boundary for properties ..................... ## [prop,xbl,4.1e8]
## X-axis Right boundary for properties .................... ## [prop,xbr,12.e8]
## Nuclear network ......................................... ## [network,fluid1,fluid2]
[]
## Temperature stratification .............................. ## [temp,False,4.e8,12.e8,3.8e9,0.8e9,0]
## Brunt-Vaisalla frequency ................................ ## [nsq,False,4.e8,12.e8,1.5,-0.15,0]
## Turbulent Kinetic Energy Stratification ................. ## [tkie,False,4.e8,12.e8,2.5e14,0.,0]
## Internal Energy Flux Stratification ..................... ## [eintflx,False,4.e8,12.e8,0.7e28,-0.5e27,0]
## Entropy Flux Stratification ............................. ## [entrflx,False,4.e8,12.e8,0.1e17,-1.e17,0]
## Pressure X Flux Stratification .......................... ## [pressxflx,False,4.e8,12.e8,2.e26,-3.e26,0]
## Temperature Flux Stratification ......................... ## [tempflx,False,4.e8,12.e8,0.8e14,-1.e13,0]
## Enthalpy Flux Stratification ............................ ## [enthflx,False,4.e8,12.e8,1.3e28,-1.e27,0]
## Turbulent Mass Flux Stratification ...................... ## [tmsflx,False,4.e8,12.e8,4.e9,-3.5e10,0]
## Turbulent Radial Velocity RMS ........................... ## [uxrms,True,4.e8,12.e8,1.7e7,-1.e6,0]
## Turbulent Uy Velocity RMS ............................... ## [uyrms,True,4.e8,12.e8,1.7e7,-1.e6,0]
## Turbulent Uz Velocity RMS ............................... ## [uzrms,True,4.e8,12.e8,1.7e7,-1.e6,0]
## Buoyancy ................................................ ## [buoy,True,4.e8,12.e8,1.2e8,-0.1e8,0]
## Density Fluctuations (RMS) amplitude .................... ## [ddrms,True,4.e8,12.e8,3.e-1,1.e-3,0]
[]
## Fluid1rons stratification ............................... ## [xrho_fluid1,False,4.e8,12.e8,1.1,-0.1,0]
## Fluid1rons flux X stratification ........................ ## [xflxx_fluid1,False,4.e8,12.e8,3.e10,-1.e9,0]
[]
## Fluid2rons stratification ............................... ## [xrho_fluid2,False,4.e8,12.e8,1.1,-0.1,0]
## Fluid2rons flux X stratification ........................ ## [xflxx_fluid2,False,4.e8,12.e8,1.e9,-3.e10,0]