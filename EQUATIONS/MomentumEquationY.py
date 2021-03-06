import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import UTILS.CALCULUS as calc
import UTILS.ALIMIT as al

# Theoretical background https://arxiv.org/abs/1401.5176

# Mocak, Meakin, Viallet, Arnett, 2014, Compressible Hydrodynamic Mean-Field #
# Equations in Spherical Geometry and their Application to Turbulent Stellar #
# Convection Data #

class MomentumEquationY(calc.CALCULUS,al.ALIMIT,object):

    def __init__(self,filename,ig,intc,data_prefix):
        super(MomentumEquationY,self).__init__(ig) 
	
        # load data to structured array
        eht = np.load(filename)		

        # load grid
        xzn0   = np.asarray(eht.item().get('xzn0')) 	

        # pick equation-specific Reynolds-averaged mean fields according to:
        # https://github.com/mmicromegas/ransX/blob/master/DOCS/ransXimplementationGuide.pdf	

        dd = np.asarray(eht.item().get('dd')[intc])		
        pp = np.asarray(eht.item().get('pp')[intc])
		
        ddux = np.asarray(eht.item().get('ddux')[intc])
        dduy = np.asarray(eht.item().get('dduy')[intc])
		
        dduxuy = np.asarray(eht.item().get('dduxuy')[intc])
        dduzuz = np.asarray(eht.item().get('dduzuz')[intc])		
        dduzuzcoty = np.asarray(eht.item().get('dduzuzcoty')[intc])

        gradypp = np.asarray(eht.item().get('gradypp')[intc])
		
        # store time series for time derivatives
        t_timec   = np.asarray(eht.item().get('timec'))		
        t_dd      = np.asarray(eht.item().get('dd')) 
        t_dduy    = np.asarray(eht.item().get('dduy')) 				
		
        # construct equation-specific mean fields
        fht_ux = ddux/dd  		
        fht_uy = dduy/dd 		
        ryx    = dduxuy - ddux*dduy/dd
		
        #####################
        # Y MOMENTUM EQUATION 
        #####################

        # LHS -dq/dt 		
        self.minus_dt_dduy = -self.dt(t_dduy,xzn0,t_timec,intc)
     
        # LHS -div rho fht_ux fht_ux
        self.minus_div_eht_dd_fht_ux_fht_uy = -self.Div(dd*fht_ux*fht_uy,xzn0)	 
		 
        # RHS -div ryx
        self.minus_div_ryx = -self.Div(ryx,xzn0)
		
        # RHS -G
        self.minus_G = -(dduxuy - dduzuzcoty)/xzn0
		
        # RHS -1/r grady_pp		
        self.minus_1_o_grady_pp = -(1./xzn0)*gradypp 
		
        # -res
        self.minus_resResYmomentumEquation = \
          -(self.minus_dt_dduy + self.minus_div_eht_dd_fht_ux_fht_uy + self.minus_div_ryx \
            + self.minus_G + self.minus_1_o_grady_pp)
		
        #########################
        # END Y MOMENTUM EQUATION 
        #########################		
		
        # assign global data to be shared across whole class
        self.data_prefix = data_prefix		
        self.xzn0        = xzn0
        self.dduy        = dduy	
		
    def plot_momentum_y(self,LAXIS,xbl,xbr,ybu,ybd,ilg):
        """Plot dduy stratification in the model""" 
		
        # load x GRID
        grd1 = self.xzn0

        # load DATA to plot
        plt1 = self.dduy
		
        # create FIGURE
        plt.figure(figsize=(7,6))
		
        # format AXIS, make sure it is exponential
        plt.gca().yaxis.get_major_formatter().set_powerlimits((0,0))		
		
        # set plot boundaries   
        to_plot = [plt1]		
        self.set_plt_axis(LAXIS,xbl,xbr,ybu,ybd,to_plot)
			
        # plot DATA 
        plt.title('dduy')
        plt.plot(grd1,plt1,color='brown',label = r'$\overline{\rho} \widetilde{u}_y$')
		
        # define and show x/y LABELS
        setxlabel = r"r (cm)"
        setylabel = r"$\overline{\rho} \widetilde{u}_y$ (g cm$^{-2}$ s$^{-1}$)"

        plt.xlabel(setxlabel)
        plt.ylabel(setylabel)
		
        # show LEGEND
        plt.legend(loc=ilg,prop={'size':18})

        # display PLOT
        plt.show(block=False)

        # save PLOT
        plt.savefig('RESULTS/'+self.data_prefix+'mean_dduy.png')
	
    def plot_momentum_equation_y(self,LAXIS,xbl,xbr,ybu,ybd,ilg):
        """Plot momentum y equation in the model""" 
		
        # load x GRID
        grd1 = self.xzn0

        lhs0 = self.minus_dt_dduy
        lhs1 = self.minus_div_eht_dd_fht_ux_fht_uy
		
        rhs0 = self.minus_div_ryx 
        rhs1 = self.minus_G
        rhs2 = self.minus_1_o_grady_pp
		
        res = self.minus_resResYmomentumEquation
				
        # create FIGURE
        plt.figure(figsize=(7,6))
		
        # format AXIS, make sure it is exponential
        plt.gca().yaxis.get_major_formatter().set_powerlimits((0,0))		
		
        # set plot boundaries   
        to_plot = [lhs0,lhs1,rhs0,rhs1,rhs2,res]		
        self.set_plt_axis(LAXIS,xbl,xbr,ybu,ybd,to_plot)
		
        # plot DATA 
        plt.title('y momentum equation')
        plt.plot(grd1,lhs0,color='c',label = r"$-\partial_t ( \overline{\rho} \widetilde{u}_\theta ) $")
        plt.plot(grd1,lhs1,color='m',label = r"$-\nabla_r (\overline{\rho} \widetilde{u}_r \widetilde{u}_\theta ) $")		
        plt.plot(grd1,rhs0,color='b',label=r"$-\nabla_r (\widetilde{R}_{\theta r})$")
        plt.plot(grd1,rhs1,color='g',label=r"$-\overline{G^{M}_\theta}$")
        plt.plot(grd1,rhs2,color='r',label=r"$-(1/r) \overline{\partial_\theta P}$")		
        plt.plot(grd1,res,color='k',linestyle='--',label='res')

        # define and show x/y LABELS
        setxlabel = r"r (cm)"
        setylabel = r"g cm$^{-2}$  s$^{-2}$"
        plt.xlabel(setxlabel)
        plt.ylabel(setylabel)
		
        # show LEGEND
        plt.legend(loc=ilg,prop={'size':12})

        # display PLOT
        plt.show(block=False)

        # save PLOT
        plt.savefig('RESULTS/'+self.data_prefix+'momentum_y_eq.png')			
		



		
		
