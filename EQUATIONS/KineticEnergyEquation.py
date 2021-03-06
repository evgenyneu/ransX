import numpy as np
import matplotlib.pyplot as plt
import UTILS.CALCULUS as calc
import UTILS.ALIMIT as al

# Theoretical background https://arxiv.org/abs/1401.5176

# Mocak, Meakin, Viallet, Arnett, 2014, Compressible Hydrodynamic Mean-Field #
# Equations in Spherical Geometry and their Application to Turbulent Stellar #
# Convection Data #

class KineticEnergyEquation(calc.CALCULUS,al.ALIMIT,object):

    def __init__(self,filename,ig,intc,minus_kolmrate,data_prefix):
        super(KineticEnergyEquation,self).__init__(ig) 
	
        # load data to structured array
        eht = np.load(filename)		

        # load grid
        xzn0   = np.asarray(eht.item().get('xzn0')) 	

        # pick equation-specific Reynolds-averaged mean fields according to:
        # https://github.com/mmicromegas/ransX/blob/master/DOCS/ransXimplementationGuide.pdf		
		
        dd        = np.asarray(eht.item().get('dd')[intc])
        ux        = np.asarray(eht.item().get('ux')[intc])	
        pp        = np.asarray(eht.item().get('pp')[intc])		
		
        ddux      = np.asarray(eht.item().get('ddux')[intc])
        dduy      = np.asarray(eht.item().get('dduy')[intc])
        dduz      = np.asarray(eht.item().get('dduz')[intc])		
		
        dduxux    = np.asarray(eht.item().get('dduxux')[intc])
        dduyuy    = np.asarray(eht.item().get('dduyuy')[intc])
        dduzuz    = np.asarray(eht.item().get('dduzuz')[intc])
        dduxuy    = np.asarray(eht.item().get('dduxuy')[intc])
        dduxuz    = np.asarray(eht.item().get('dduxuz')[intc])
		
        ddekux	   = np.asarray(eht.item().get('ddekux')[intc])	
        ddek      = np.asarray(eht.item().get('ddek')[intc])		
		
        ppdivu    = np.asarray(eht.item().get('ppdivu')[intc])
        divu      = np.asarray(eht.item().get('divu')[intc])
        ppux      = np.asarray(eht.item().get('ppux')[intc])		

        #########################
        # KINETIC ENERGY EQUATION 
        #########################  			
		
        # store time series for time derivatives
        t_timec   = np.asarray(eht.item().get('timec')) 
        t_dd      = np.asarray(eht.item().get('dd'))

        t_ddux = np.asarray(eht.item().get('ddux'))
        t_dduy = np.asarray(eht.item().get('dduy'))
        t_dduz = np.asarray(eht.item().get('dduz'))		
		
        t_dduxux = np.asarray(eht.item().get('dduxux'))
        t_dduyuy = np.asarray(eht.item().get('dduyuy'))
        t_dduzuz = np.asarray(eht.item().get('dduzuz'))

        t_fht_ek = 0.5*(t_dduxux+t_dduyuy+t_dduzuz)/t_dd		
		
        # construct equation-specific mean fields		
        fht_ux = ddux/dd
        fht_ek = 0.5*(dduxux + dduyuy + dduzuz)/dd
        fekx   = ddekux - dd*fht_ek*fht_ux
        fpx    = ppux - pp*ux		
		
        uxffuxff = (dduxux/dd - ddux*ddux/(dd*dd)) 
        uyffuyff = (dduyuy/dd - dduy*dduy/(dd*dd)) 
        uzffuzff = (dduzuz/dd - dduz*dduz/(dd*dd)) 			
		
        # LHS -dq/dt 			
        self.minus_dt_eht_dd_fht_ek = -self.dt(t_dd*t_fht_ek,xzn0,t_timec,intc)

        # LHS -div dd ux ke
        self.minus_div_eht_dd_fht_ux_fht_ek = -self.Div(dd*fht_ux*fht_ek,xzn0)
		
        # -div kinetic energy flux
        self.minus_div_fekx  = -self.Div(fekx,xzn0)

        # -div acoustic flux		
        self.minus_div_fpx = -self.Div(fpx,xzn0)		
		
        # RHS warning ax = overline{+u''_x} 
        self.plus_ax = -ux + fht_ux		
		
        # +buoyancy work
        self.plus_wb = self.plus_ax*self.Grad(pp,xzn0)
		
        # +pressure dilatation
        self.plus_wp = ppdivu-pp*divu
				
        # -R grad u
		
        rxx = dduxux - ddux*ddux/dd
        rxy = dduxuy - ddux*dduy/dd
        rxz = dduxuz - ddux*dduz/dd
		
        self.minus_r_grad_u = -(rxx*self.Grad(ddux/dd,xzn0) + \
                                rxy*self.Grad(dduy/dd,xzn0) + \
                                rxz*self.Grad(dduz/dd,xzn0))
		
        # -dd Dt ke
        t_fht_ux = t_ddux/t_dd		
        t_fht_uy = t_dduy/t_dd	
        t_fht_uz = t_dduz/t_dd	

        fht_ux = ddux/dd		
        fht_uy = dduy/dd	
        fht_uz = dduz/dd
		
        self.minus_dd_Dt_fht_ui_fht_ui = \
            -self.dt(t_dd*(t_fht_ux**2.+t_fht_uy**2.+t_fht_uz**2.),xzn0,t_timec,intc) - \
             self.Div(dd*fht_ux*(fht_ux**2.+fht_uy**2.+fht_uz**2.),xzn0)
		
        # -res		
        self.minus_resKeEquation = - (self.minus_dt_eht_dd_fht_ek + self.minus_div_eht_dd_fht_ux_fht_ek + \
                                      self.plus_wb + self.plus_wp + self.minus_div_fekx + \
	                                  self.minus_div_fpx + self.minus_r_grad_u + \
                                      self.minus_dd_Dt_fht_ui_fht_ui)

									   				
        # - kolm_rate u'3/lc
        self.minus_kolmrate = minus_kolmrate 		
													
        #############################
        # END KINETIC ENERGY EQUATION 
        ############################# 		
			
        # assign global data to be shared across whole class
        self.data_prefix = data_prefix		
        self.xzn0        = xzn0
        self.dd          = dd
        self.fht_ek      = fht_ek			
			
			
    def plot_ke(self,LAXIS,xbl,xbr,ybu,ybd,ilg):
        """Plot kinetic energy stratification in the model""" 
		
        # load x GRID
        grd1 = self.xzn0
	
        # load DATA to plot 		
        plt1 = self.fht_ek
		
        # create FIGURE
        plt.figure(figsize=(7,6))
		
        # format AXIS, make sure it is exponential
        plt.gca().yaxis.get_major_formatter().set_powerlimits((0,0))		
		
        # set plot boundaries   
        to_plot = [plt1]		
        self.set_plt_axis(LAXIS,xbl,xbr,ybu,ybd,to_plot)		
				
        # plot DATA 
        plt.title('kinetic energy')
        plt.plot(grd1,plt1,color='brown',label = r'$\frac{1}{2} \widetilde{u_i u_i}$')

        # define and show x/y LABELS
        setxlabel = r"r (cm)"
        setylabel = r"$\widetilde{\epsilon}_K$ (erg g$^{-1}$)"
        plt.xlabel(setxlabel)
        plt.ylabel(setylabel)
		
        # show LEGEND
        plt.legend(loc=ilg,prop={'size':18})

        # display PLOT
        plt.show(block=False)

        # save PLOT
        plt.savefig('RESULTS/'+self.data_prefix+'mean_ek.png')		

    def plot_ke_equation(self,LAXIS,xbl,xbr,ybu,ybd,ilg):
        """Plot kinetic energy equation in the model""" 
		
        # load x GRID
        grd1 = self.xzn0

        lhs0 = self.minus_dt_eht_dd_fht_ek
        lhs1 = self.minus_div_eht_dd_fht_ux_fht_ek
		
        rhs0 = self.plus_wb
        rhs1 = self.plus_wp		
        rhs2 = self.minus_div_fekx
        rhs3 = self.minus_div_fpx
        rhs4 = self.minus_r_grad_u
        rhs5 = self.minus_dd_Dt_fht_ui_fht_ui		
		
        res = self.minus_resKeEquation
		
        rhs6 = self.minus_kolmrate*self.dd		
		
        # create FIGURE
        plt.figure(figsize=(7,6))
		
        # set plot boundaries   
        to_plot = [lhs0,lhs1,rhs0,rhs1,rhs2,rhs3,rhs4,rhs5,rhs6,res]		
        self.set_plt_axis(LAXIS,xbl,xbr,ybu,ybd,to_plot)		
		
        # format AXIS, make sure it is exponential
        plt.gca().yaxis.get_major_formatter().set_powerlimits((0,0))		
		
        # plot DATA 
        plt.title('kinetic energy equation')
        plt.plot(grd1,-lhs0,color='#FF6EB4',label = r'$-\partial_t (\overline{\rho} \widetilde{\epsilon}_K)$')
        plt.plot(grd1,-lhs1,color='k',label = r"$-\nabla_r (\overline{\rho} \widetilde{u}_r \widetilde{\epsilon}_K)$")	
		
        plt.plot(grd1,rhs0,color='r',label = r'$+W_b$')     
        plt.plot(grd1,rhs1,color='c',label = r'$+W_p$') 
        plt.plot(grd1,rhs2,color='#802A2A',label = r"$-\nabla_r f_k$") 
        plt.plot(grd1,rhs3,color='m',label = r"$-\nabla_r f_P$")
        plt.plot(grd1,rhs4,color='b',label = r"$-\widetilde{R}_{ri}\partial_r \widetilde{u_i}$")
        plt.plot(grd1,rhs5,color='g',label=r"$-\overline{\rho}\widetilde{D}_t \widetilde{u}_i \widetilde{u}_i$")		
        plt.plot(grd1,rhs6,color='k',linewidth=0.7,label = r"$-\overline{\rho} u^{'3}_{rms}/l_c$")		
        plt.plot(grd1,res,color='k',linestyle='--',label=r"res $\sim N_{\epsilon_K}$")
 
        # define and show x/y LABELS
        setxlabel = r"r (cm)"
        setylabel = r"erg cm$^{-3}$ s$^{-1}$"
        plt.xlabel(setxlabel)
        plt.ylabel(setylabel)
		
        # show LEGEND
        plt.legend(loc=1,prop={'size':8})

        # display PLOT
        plt.show(block=False)

        # save PLOT
        plt.savefig('RESULTS/'+self.data_prefix+'ek_eq.png')	
	
    def tke_dissipation(self):
        return self.minus_resTkeEquation		

    def tke(self):
        return self.tke		
		
