import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import UTILS.CALCULUS as calc
import UTILS.ALIMIT as al

# Theoretical background https://arxiv.org/abs/1401.5176

# Mocak, Meakin, Viallet, Arnett, 2014, Compressible Hydrodynamic Mean-Field #
# Equations in Spherical Geometry and their Application to Turbulent Stellar #
# Convection Data #

class HsseContinuityEquation(calc.CALCULUS,al.ALIMIT,object):

    def __init__(self,filename,ig,intc,data_prefix):
        super(HsseContinuityEquation,self).__init__(ig) 
	
        # load data to structured array
        eht = np.load(filename)		

        # load grid
        nx = np.asarray(eht.item().get('nx'))
        xzn0 = np.asarray(eht.item().get('xzn0')) 	
        xznl = np.asarray(eht.item().get('xznl')) 
        xznr = np.asarray(eht.item().get('xznr')) 
		
        # pick equation-specific Reynolds-averaged mean fields according to:
        # https://github.com/mmicromegas/ransX/blob/master/DOCS/ransXimplementationGuide.pdf	

        mm    = np.asarray(eht.item().get('mm')[intc])			
        dd    = np.asarray(eht.item().get('dd')[intc])
        ux    = np.asarray(eht.item().get('ux')[intc])			
        pp    = np.asarray(eht.item().get('pp')[intc])	
        gg    = np.asarray(eht.item().get('gg')[intc])
        ddux  = np.asarray(eht.item().get('ddux')[intc])		
		
        dduxux    = np.asarray(eht.item().get('dduxux')[intc])
        uxdivu    = np.asarray(eht.item().get('uxdivu')[intc])
        divu    = np.asarray(eht.item().get('divu')[intc])

        gamma1    = np.asarray(eht.item().get('gamma1')[intc])
		
        # store time series for time derivatives
        t_timec   = np.asarray(eht.item().get('timec'))		
        t_dd      = np.asarray(eht.item().get('dd')) 	
        t_ux      = np.asarray(eht.item().get('ux')) 
        t_ddux    = np.asarray(eht.item().get('ddux')) 		
		
        t_eht_uxff = (t_ddux-t_dd*t_ux)/t_dd 	
	
        #t_mm    = np.asarray(eht.item().get('mm')) 		
        #minus_dt_mm = -self.dt(t_mm,xzn0,t_timec,intc)
        #fht_ux = minus_dt_mm/(4.*np.pi*(xzn0**2.)*dd)	
	
        # construct equation-specific mean fields
        fht_ux = ddux/dd			
        fdd = ddux-dd*ux
        fht_rxx = dduxux - ddux*ddux/dd
        fdil = (uxdivu - ux*divu) 		
	
        #####################
        # CONTINUITY EQUATION 
        #####################
				
        # LHS -gradx mm
        self.minus_gradx_mm = -self.Grad(dd*(4./3.)*np.pi*(xzn0**3),xzn0)
				
        # RHS +4 pi r^2 dd
        self.plus_four_pi_rsq_dd = +4.*np.pi*(xzn0**2.)*dd
    		
        # scale factor +4 pi r^3/ 3 fht_ux
        self.plus_four_pi_rcu_o_three_fht_ux = (4./3.)*np.pi*(xzn0**3)/fht_ux  		

        # RHS -4 pi r^3/ 3 fht_ux Div fdd
        self.minus_four_pi_rcu_o_three_fht_ux_div_fdd = -self.plus_four_pi_rcu_o_three_fht_ux*self.Div(fdd,xzn0)
		
        # RHS +4 pi r^3/ 3 fht_ux fdd_o_dd gradx dd				
        self.plus_four_pi_rcu_o_three_fht_ux_fdd_o_dd_gradx_dd = +self.plus_four_pi_rcu_o_three_fht_ux*(fdd/dd)*self.Grad(dd,xzn0)		

        # RHS -4 pi r^3/ 3 fht_ux dd Div ux 
        self.minus_four_pi_rcu_o_three_fht_ux_dd_div_ux = -self.plus_four_pi_rcu_o_three_fht_ux*dd*self.Div(ux,xzn0) 
		
        # RHS -dq/dt 		
        self.minus_four_pi_rcu_o_three_fht_ux_dt_dd = -self.plus_four_pi_rcu_o_three_fht_ux*self.dt(t_dd,xzn0,t_timec,intc)

        # -res
        self.minus_resContEquation = -(self.minus_gradx_mm+self.plus_four_pi_rsq_dd+\
          self.minus_four_pi_rcu_o_three_fht_ux_div_fdd+self.plus_four_pi_rcu_o_three_fht_ux_fdd_o_dd_gradx_dd+\
           self.minus_four_pi_rcu_o_three_fht_ux_dd_div_ux+self.minus_four_pi_rcu_o_three_fht_ux_dt_dd)
		
        #########################	
        # END CONTINUITY EQUATION
        #########################
		
        #################################
        # ALTERNATIVE CONTINUITY EQUATION 
        #################################				
		
        # RHS -mm_dd_eht_fdil/fht_rxx  		
        self.minus_mm_dd_fdil_o_fht_rxx = -(4./3)*np.pi*(xzn0**3.)*dd*dd*fdil/fht_rxx		
		
        # -res		
        self.minus_resContEquation2 = -(self.minus_gradx_mm+self.plus_four_pi_rsq_dd+self.minus_mm_dd_fdil_o_fht_rxx)		
		
        #####################################
        # END ALTERNATIVE CONTINUITY EQUATION 
        #####################################  		
		
        ############################################
        # ALTERNATIVE CONTINUITY EQUATION SIMPLIFIED
        ############################################		
			
        gg = -gg			
			
        # RHS +dd_mm_gg_o_gamma1_pp	- the plus sign is due to gg
        self.minus_dd_mm_gg_o_gamma1_pp = -dd*(4./3)*np.pi*(xzn0**3.)*dd*gg/(gamma1*pp)		
		
        # -res		
        self.minus_resContEquation3 = -(self.minus_gradx_mm+self.plus_four_pi_rsq_dd+self.minus_dd_mm_gg_o_gamma1_pp)		
		
        ################################################
        # END ALTERNATIVE CONTINUITY EQUATION SIMPLIFIED
        ################################################		
		
        self.dt_eht_uxff = self.dt(t_eht_uxff,xzn0,t_timec,intc)		
        self.div_fht_rxx_o_dd = self.Div(fht_rxx/dd,xzn0)
		
        # CRACKING ON VELOCITIES		
        self.plus_dt_mm = -4.*np.pi*(xzn0**2.)*dd*fht_ux		
        self.plus_gradx_mm = +self.Grad(dd*(4./3.)*np.pi*(xzn0**3),xzn0)
        self.plus_gradx_dd_o_three_dd_fht_ux = +self.Grad(dd,xzn0)/(3.*dd*fht_ux)		
		
        # assign global data to be shared across whole class
        self.data_prefix = data_prefix		
        self.xzn0        = xzn0
        self.dd          = dd
        self.fdil        = fdil
        self.dd = dd	
        self.fht_ux = fht_ux		
		
		
    def plot_rho(self,LAXIS,xbl,xbr,ybu,ybd,ilg):
        """Plot rho stratification in the model""" 
		
        # load x GRID
        grd1 = self.xzn0
	
        # load DATA to plot
        plt1 = self.dd
		
        # create FIGURE
        plt.figure(figsize=(7,6))
		
        # format AXIS, make sure it is exponential
        plt.gca().yaxis.get_major_formatter().set_powerlimits((0,0))		
		
        # set plot boundaries   
        to_plot = [plt1]		
        self.set_plt_axis(LAXIS,xbl,xbr,ybu,ybd,to_plot)	
		
        # plot DATA 
        plt.title('density')
        plt.plot(grd1,plt1,color='brown',label = r'$\overline{\rho}$')

        # define and show x/y LABELS
        setxlabel = r"r (cm)"
        setylabel = r"$\overline{\rho}$ (g cm$^{-3}$)"

        plt.xlabel(setxlabel)
        plt.ylabel(setylabel)
		
        # show LEGEND
        plt.legend(loc=ilg,prop={'size':18})

        # display PLOT
        plt.show(block=False)

        # save PLOT
        plt.savefig('RESULTS/'+self.data_prefix+'mean_rho.png')
	
    def plot_continuity_equation(self,LAXIS,xbl,xbr,ybu,ybd,ilg):
        """Plot continuity equation in the model""" 
		
        # load x GRID
        grd1 = self.xzn0

        lhs0 = self.minus_gradx_mm
		
        rhs0 = self.plus_four_pi_rsq_dd		
        rhs1 = self.minus_four_pi_rcu_o_three_fht_ux_div_fdd
        rhs2 = self.plus_four_pi_rcu_o_three_fht_ux_fdd_o_dd_gradx_dd
        rhs3 = self.minus_four_pi_rcu_o_three_fht_ux_dd_div_ux
        rhs4 = self.minus_four_pi_rcu_o_three_fht_ux_dt_dd		
		
        res = self.minus_resContEquation
		
        # create FIGURE
        plt.figure(figsize=(7,6))
		
        # format AXIS, make sure it is exponential
        plt.gca().yaxis.get_major_formatter().set_powerlimits((0,0))		
		
        # set plot boundaries   
        to_plot = [lhs0,rhs0,rhs1,rhs2,rhs3,rhs4,res]		
        self.set_plt_axis(LAXIS,xbl,xbr,ybu,ybd,to_plot)
		
        # plot DATA 
        plt.title('hsse continuity equation')
        plt.plot(grd1,lhs0,color='g',label = r'$-\partial_r (\overline{m})$')
        plt.plot(grd1,rhs0,color='r',label = r"$+4 \pi r^2 \overline{\rho}$")
        plt.plot(grd1,rhs1,color='c',label = r"$-(4 \pi r^3/3 \widetilde{u}_r) \nabla_r f_\rho$")		
        plt.plot(grd1,rhs2,color='m',label = r"$+(4 \pi r^3/3 \widetilde{u}_r) f_\rho / \overline{\rho} \partial_r \overline{\rho}$")
        plt.plot(grd1,rhs3,color='b',label=r"$-(4 \pi r^3/3 \widetilde{u}_r) \overline{\rho} \overline{d}$")
        plt.plot(grd1,rhs4,color='y',label=r"$-(4 \pi r^3/3 \widetilde{u}_r) \partial_t \overline{\rho}$")
        plt.plot(grd1,res,color='k',linestyle='--',label='res')

        # define and show x/y LABELS
        setxlabel = r"r (cm)"
        setylabel = r"g cm$^{-1}$"
        plt.xlabel(setxlabel)
        plt.ylabel(setylabel)
		
        # show LEGEND
        plt.legend(loc=ilg,prop={'size':9})

        # display PLOT
        plt.show(block=False)

        # save PLOT
        plt.savefig('RESULTS/'+self.data_prefix+'hsse_continuity_eq.png')
		
		
    def plot_continuity_equation_2(self,LAXIS,xbl,xbr,ybu,ybd,ilg):
        """Plot continuity equation in the model""" 
		
        # load x GRID
        grd1 = self.xzn0

        lhs0 = self.minus_gradx_mm
		
        rhs0 = self.plus_four_pi_rsq_dd		
        rhs1 = self.minus_mm_dd_fdil_o_fht_rxx
		
		
        res = self.minus_resContEquation2
		
        # create FIGURE
        plt.figure(figsize=(7,6))
		
        # format AXIS, make sure it is exponential
        plt.gca().yaxis.get_major_formatter().set_powerlimits((0,0))		
		
        # set plot boundaries   
        to_plot = [lhs0,rhs0,rhs1,res]		
        self.set_plt_axis(LAXIS,xbl,xbr,ybu,ybd,to_plot)
		
        # plot DATA 
        plt.title('alternative hsse continuity equation')
        plt.plot(grd1,lhs0,color='g',label = r'$-\partial_r (\overline{m})$')
        plt.plot(grd1,rhs0,color='r',label = r"$+4 \pi r^2 \overline{\rho}$")
        plt.plot(grd1,rhs1,color='b',label = r"$-\overline{\rho} \ \overline{m} \ \overline{u'_r d''} / \ \widetilde{R}_{rr}$")		
        plt.plot(grd1,res,color='k',linestyle='--',label = r"res")		
		
        # define and show x/y LABELS
        setxlabel = r"r (cm)"
        setylabel = r"g cm$^{-1}$"
        plt.xlabel(setxlabel)
        plt.ylabel(setylabel)
		
        # show LEGEND
        plt.legend(loc=ilg,prop={'size':12})

        # display PLOT
        plt.show(block=False)

        # save PLOT
        plt.savefig('RESULTS/'+self.data_prefix+'hsse_continuity_eq_alternative.png')		
				
				
    def plot_continuity_equation_3(self,LAXIS,xbl,xbr,ybu,ybd,ilg):
        """Plot continuity equation in the model""" 
		
        # load x GRID
        grd1 = self.xzn0

        lhs0 = self.minus_gradx_mm
		
        rhs0 = self.plus_four_pi_rsq_dd			
        rhs1 = self.minus_dd_mm_gg_o_gamma1_pp		
		
        res = self.minus_resContEquation3
		
        # create FIGURE
        plt.figure(figsize=(7,6))
		
        # format AXIS, make sure it is exponential
        plt.gca().yaxis.get_major_formatter().set_powerlimits((0,0))		
		
        # set plot boundaries   
        to_plot = [lhs0,rhs0,rhs1,res]		
        self.set_plt_axis(LAXIS,xbl,xbr,ybu,ybd,to_plot)
		
        # plot DATA 
        plt.title('alternative hsse continuity eq simp')
        plt.plot(grd1,lhs0,color='g',label = r'$-\partial_r (\overline{m})$')
        plt.plot(grd1,rhs0,color='r',label = r"$+4 \pi r^2 \overline{\rho}$")		
        plt.plot(grd1,rhs1,color='b',label = r"$-\overline{\rho} \ \overline{m} \ \overline{g}_r / \Gamma_1 \overline{P}$")		
        plt.plot(grd1,res,color='k',linestyle='--',label = r"res")		
		
        # define and show x/y LABELS
        setxlabel = r"r (cm)"
        setylabel = r"g cm$^{-1}$"
        plt.xlabel(setxlabel)
        plt.ylabel(setylabel)
		
        # show LEGEND
        plt.legend(loc=ilg,prop={'size':14})

        # display PLOT
        plt.show(block=False)

        # save PLOT
        plt.savefig('RESULTS/'+self.data_prefix+'hsse_continuity_eq_alternative_simplified.png')		

    def plot_velocities(self,LAXIS,xbl,xbr,ybu,ybd,ilg):
        """Plot continuity equation in the model""" 
		
        # load x GRID
        grd1 = self.xzn0

        lhs0 = -self.plus_gradx_mm/self.plus_dt_mm
		
        rhs0 = self.plus_four_pi_rsq_dd/self.plus_dt_mm			
        rhs1 = self.minus_dd_mm_gg_o_gamma1_pp/self.plus_dt_mm		
		
        res = lhs0+rhs0+rhs1
		
        # create FIGURE
        plt.figure(figsize=(7,6))
		
        # format AXIS, make sure it is exponential
        plt.gca().yaxis.get_major_formatter().set_powerlimits((0,0))		
		
        # set plot boundaries   
        to_plot = [lhs0,rhs0,rhs1,res]		
        self.set_plt_axis(LAXIS,xbl,xbr,ybu,ybd,to_plot)
		
        # plot DATA 
        plt.title('velocities')
        plt.plot(grd1,lhs0,color='g',label = r'$-\partial_r (\overline{m})/\partial_t (\overline{M})$')
        plt.plot(grd1,rhs0,color='r',label = r"$+4 \pi r^2 \overline{\rho} / \partial_t (\overline{M})$")		
        plt.plot(grd1,rhs1,color='b',label = r"$-\overline{\rho} \ \overline{m} \ \overline{g}_r / \Gamma_1 \overline{P}\partial_t (\overline{M})$")		
        plt.plot(grd1,res,color='k',linestyle='--',label = r"res")		
		
        # define and show x/y LABELS
        setxlabel = r"r (cm)"
        setylabel = r"g cm$^{-1}$"
        plt.xlabel(setxlabel)
        plt.ylabel(setylabel)
		
        # show LEGEND
        plt.legend(loc=ilg,prop={'size':14})

        lhs0 = +1./self.fht_ux - self.plus_gradx_dd_o_three_dd_fht_ux
		
        rhs0 = self.plus_four_pi_rsq_dd/self.plus_dt_mm			
        rhs1 = self.minus_dd_mm_gg_o_gamma1_pp/self.plus_dt_mm		
		
        res = lhs0+rhs0+rhs1		
		
        # create FIGURE
        plt.figure(figsize=(7,6))
		
        # format AXIS, make sure it is exponential
        plt.gca().yaxis.get_major_formatter().set_powerlimits((0,0))		
		
        # set plot boundaries   
        to_plot = [lhs0,rhs0,rhs1,res]		
        self.set_plt_axis(LAXIS,xbl,xbr,ybu,ybd,to_plot)
		
        # plot DATA 
        plt.title('velocities')
        plt.plot(grd1,lhs0,color='g',label = r'$-1/\widetilde{u}_r$')
        plt.plot(grd1,rhs0,color='r',label = r"$+4 \pi r^2 \overline{\rho} / \partial_t (\overline{M})$")		
        plt.plot(grd1,rhs1,color='b',label = r"$-\overline{\rho} \ \overline{m} \ \overline{g}_r / \Gamma_1 \overline{P}\partial_t (\overline{M})$")		
        plt.plot(grd1,res,color='k',linestyle='--',label = r"res")		
		
        # define and show x/y LABELS
        setxlabel = r"r (cm)"
        setylabel = r"g cm$^{-1}$"
        plt.xlabel(setxlabel)
        plt.ylabel(setylabel)
		
        # show LEGEND
        plt.legend(loc=ilg,prop={'size':14})		
		
		
        # display PLOT
        plt.show(block=False)

        # save PLOT
        plt.savefig('RESULTS/'+self.data_prefix+'hsse_velexperiment.png')	
		
    def plot_dilatation_flux(self,LAXIS,xbl,xbr,ybu,ybd,ilg):
        """Plot dilatation flux in the model""" 
		
        # load x GRID
        grd1 = self.xzn0

        #lhs0 = self.dd*self.fdil
        lhs0 = self.fdil
        lhs1 = self.dt_eht_uxff
        lhs2 = self.div_fht_rxx_o_dd		
		

        # create FIGURE
        plt.figure(figsize=(7,6))
		
        # format AXIS, make sure it is exponential
        plt.gca().yaxis.get_major_formatter().set_powerlimits((0,0))		
		
        # set plot boundaries   
        to_plot = [lhs0]		
        self.set_plt_axis(LAXIS,xbl,xbr,ybu,ybd,to_plot)
		
        # plot DATA 
        plt.title('dilatation flux')
        #plt.plot(grd1,lhs0,color='r',label = r"$\overline{\rho} \overline{u'_r d''}$")
        plt.plot(grd1,lhs0,color='r',label = r"$\overline{u'_r d''}$")
        #plt.plot(grd1,lhs1,color='b',label = r"$\partial_t \overline{u''_r}$")		
        #plt.plot(grd1,lhs2,color='g',label = r"$\nabla_r \widetilde{R}_{rr} / \overline{\rho}$")	
		
        # define and show x/y LABELS
        setxlabel = r"r (cm)"
        setylabel = r"$cm \ s^{-2}$"
        plt.xlabel(setxlabel)
        plt.ylabel(setylabel)
		
        # show LEGEND
        plt.legend(loc=ilg,prop={'size':14})

        # display PLOT
        plt.show(block=False)

        # save PLOT
        plt.savefig('RESULTS/'+self.data_prefix+'dilatation_flux.png')	
		
    def plot_mass_flux_acceleration(self,LAXIS,xbl,xbr,ybu,ybd,ilg):
        """Plot mass flux acceleration in the model""" 
		
        # load x GRID
        grd1 = self.xzn0

        #lhs0 = self.dd*self.fdil
        lhs0 = self.dd*self.fdil
        #lhs1 = self.dt_eht_uxff
        #lhs2 = self.div_fht_rxx_o_dd		
		

        # create FIGURE
        plt.figure(figsize=(7,6))
		
        # format AXIS, make sure it is exponential
        plt.gca().yaxis.get_major_formatter().set_powerlimits((0,0))		
		
        # set plot boundaries   
        to_plot = [lhs0]		
        self.set_plt_axis(LAXIS,xbl,xbr,ybu,ybd,to_plot)
		
        # plot DATA 
        plt.title('mass flux acceleration')
        plt.plot(grd1,lhs0,color='b',label = r"$\overline{\rho} \overline{u'_r d''}$")
        #plt.plot(grd1,lhs0,color='r',label = r"$\overline{u'_r d''}$")
        #plt.plot(grd1,lhs1,color='b',label = r"$\partial_t \overline{u''_r}$")		
        #plt.plot(grd1,lhs2,color='g',label = r"$\nabla_r \widetilde{R}_{rr} / \overline{\rho}$")	
		
        # define and show x/y LABELS
        setxlabel = r"r (cm)"
        setylabel = r"$g \ cm^{-2} \ s^{-2}$"
        plt.xlabel(setxlabel)
        plt.ylabel(setylabel)
		
        # show LEGEND
        plt.legend(loc=ilg,prop={'size':14})

        # display PLOT
        plt.show(block=False)

        # save PLOT
        plt.savefig('RESULTS/'+self.data_prefix+'mass_flux_acceleration.png')	

    def plot_continuity_equation_4(self,LAXIS,xbl,xbr,ybu,ybd,ilg):
        """Plot continuity equation in the model""" 
		
        # load x GRID
        grd1 = self.xzn0

        lhs0 = self.minus_gradx_mm/self.plus_dt_mm
		
        rhs0 = self.plus_four_pi_rsq_dd			
        rhs1 = self.minus_dd_mm_gg_o_gamma1_pp		
		
        res = self.minus_resContEquation3
		
        # create FIGURE
        plt.figure(figsize=(7,6))
		
        # format AXIS, make sure it is exponential
        plt.gca().yaxis.get_major_formatter().set_powerlimits((0,0))		
		
        # set plot boundaries   
        to_plot = [lhs0,rhs0,rhs1,res]		
        self.set_plt_axis(LAXIS,xbl,xbr,ybu,ybd,to_plot)
		
        # plot DATA 
        plt.title('alternative hsse continuity eq simp')
        plt.plot(grd1,lhs0,color='g',label = r'$-\partial_r (\overline{M})$')
        plt.plot(grd1,rhs0,color='r',label = r"$+4 \pi r^2 \overline{\rho}$")		
        plt.plot(grd1,rhs1,color='b',label = r"$-\overline{\rho} \ \overline{M} \ \overline{g}_r / \Gamma_1 \overline{P}$")		
        plt.plot(grd1,res,color='k',linestyle='--',label = r"res")		
		
        # define and show x/y LABELS
        setxlabel = r"r (cm)"
        setylabel = r"g cm$^{-1}$"
        plt.xlabel(setxlabel)
        plt.ylabel(setylabel)
		
        # show LEGEND
        plt.legend(loc=ilg,prop={'size':14})

        # display PLOT
        plt.show(block=False)

        # save PLOT
        plt.savefig('RESULTS/'+self.data_prefix+'hsse_continuity_eq_alternative_simplified.png')	

		