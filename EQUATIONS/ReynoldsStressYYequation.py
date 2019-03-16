import numpy as np
import matplotlib.pyplot as plt
import UTILS.CALCULUS as calc
import UTILS.ALIMIT as al

# Theoretical background https://arxiv.org/abs/1401.5176

# Mocak, Meakin, Viallet, Arnett, 2014, Compressible Hydrodynamic Mean-Field #
# Equations in Spherical Geometry and their Application to Turbulent Stellar #
# Convection Data #

class ReynoldsStressYYequation(calc.CALCULUS,al.ALIMIT,object):

    def __init__(self,filename,ig,intc,minus_kolmrate,data_prefix):
        super(ReynoldsStressYYequation,self).__init__(ig) 
	
        # load data to structured array
        eht = np.load(filename)		

        # load grid
        xzn0   = np.asarray(eht.item().get('xzn0')) 	

        # pick equation-specific Reynolds-averaged mean fields according to:
        # https://github.com/mmicromegas/ransX/blob/master/ransXtoPROMPI.pdf/ 		
		
        dd = np.asarray(eht.item().get('dd')[intc])
        ux = np.asarray(eht.item().get('ux')[intc])	
        pp = np.asarray(eht.item().get('pp')[intc])		
		
        ddux = np.asarray(eht.item().get('ddux')[intc])
        dduy = np.asarray(eht.item().get('dduy')[intc])
        dduz = np.asarray(eht.item().get('dduz')[intc])		
		
        dduycoty = np.asarray(eht.item().get('dduycoty')[intc])
        dduzcoty = np.asarray(eht.item().get('dduzcoty')[intc])		
		
        dduxux = np.asarray(eht.item().get('dduxux')[intc])
        dduyuy = np.asarray(eht.item().get('dduyuy')[intc])
        dduzuz = np.asarray(eht.item().get('dduzuz')[intc])

        dduyuycoty = np.asarray(eht.item().get('dduyuycoty')[intc])
        dduzuzcoty = np.asarray(eht.item().get('dduzuzcoty')[intc])		
		
        dduxux = np.asarray(eht.item().get('dduxux')[intc])
        dduxuy = np.asarray(eht.item().get('dduxuy')[intc])
        dduxuz = np.asarray(eht.item().get('dduxuz')[intc])

        dduxuxux = np.asarray(eht.item().get('dduxuxux')[intc])
        dduxuyuy = np.asarray(eht.item().get('dduxuyuy')[intc])
        dduxuzuz = np.asarray(eht.item().get('dduxuzuz')[intc])
		
        dduzuzuycoty = np.asarray(eht.item().get('dduzuzuycoty')[intc])		
		
        ddekux  = np.asarray(eht.item().get('ddekux')[intc])	
        ddek    = np.asarray(eht.item().get('ddek')[intc])		
		
        ppdivux = np.asarray(eht.item().get('ppdivux')[intc])
        ppdivuy = np.asarray(eht.item().get('ppdivuy')[intc])
        divux   = np.asarray(eht.item().get('divux')[intc])
        divuy   = np.asarray(eht.item().get('divuy')[intc])
        ppux    = np.asarray(eht.item().get('ppux')[intc])		

        #############################
        # REYNOLDS STRESS YY EQUATION 
        #############################   		
			
        # store time series for time derivatives
        t_timec   = np.asarray(eht.item().get('timec')) 
        t_dd      = np.asarray(eht.item().get('dd'))
		
        t_ddux    = np.asarray(eht.item().get('ddux')) 
        t_dduy    = np.asarray(eht.item().get('dduy')) 
        t_dduz    = np.asarray(eht.item().get('dduz')) 		
		
        t_dduxux = np.asarray(eht.item().get('dduxux'))
        t_dduyuy = np.asarray(eht.item().get('dduyuy'))
        t_dduzuz = np.asarray(eht.item().get('dduzuz'))
		
        t_uxffuxff = t_dduxux/t_dd - t_ddux*t_ddux/(t_dd*t_dd)
        t_uyffuyff = t_dduyuy/t_dd - t_dduy*t_dduy/(t_dd*t_dd)
        t_uzffuzff = t_dduzuz/t_dd - t_dduz*t_dduz/(t_dd*t_dd)
		
        t_ryy = t_dd*t_uyffuyff		
		
        # construct equation-specific mean fields
        fht_ux = ddux/dd
        fht_uy = dduy/dd
        fht_uz = dduz/dd		
		
        uyffuyff = (dduyuy/dd - dduy*dduy/(dd*dd)) 		
		
        ryy = dd*uyffuyff
        fkt = dduxuyuy - 2.*fht_uy*dduxuy - fht_ux*dduyuy + 2.*dd*fht_uy*fht_uy*fht_ux
		
        # LHS -dq/dt 			
        self.minus_dt_ryy = -self.dt(t_ryy,xzn0,t_timec,intc)

        # LHS -div ux ryy
        self.minus_div_fht_ux_ryy = -self.Div(fht_ux*ryy,xzn0)
		
        # -div 2 fkt 
        self.minus_div_two_fkt  = -self.Div(2.*fkt,xzn0)
		
        # +2 pressure tt dilatation
        self.plus_two_ppf_divuyff = 2.*(ppdivuy - pp*divuy)
				
        # -2 R grad u
        ryx = dduxuy - ddux*dduy/dd		
        self.minus_two_ryx_grad_fht_uy = -2.*ryx*self.Grad(fht_uy,xzn0)
		
		# +2 Gkt
        GrrT = 2.*(dduxuyuy - 2.*dduy*dduxuy/dd - fht_ux*dduyuy + 2.*fht_uy*fht_uy*fht_ux*dd)/xzn0 -\
               2.*(dduzuzuycoty - 2.*dduycoty*dduyuycoty/dd - 2.*dduycoty*dduzuzcoty/dd + \
               2.*dduzcoty*dduzcoty*dduycoty/(dd*dd))/xzn0
				 
        uyff_GtM = (dduxuzuz - fht_uy*dduxuy)/xzn0 - \
                   (dduzuzuycoty - fht_uy*dduzuzcoty)/xzn0

        self.plus_two_Gkt = 2.*((1./2.)*GrrT - uyff_GtM) 	   
		
        # -res		
        self.minus_resRyyEquation = -(self.minus_dt_ryy + self.minus_div_fht_ux_ryy + self.minus_div_two_fkt +\
                                      self.plus_two_ppf_divuyff +\
                                      self.minus_two_ryx_grad_fht_uy + self.plus_two_Gkt)
									   				
        # - kolm_rate 1/3 u'3/lc
        self.minus_onethrd_kolmrate = (1./3.)*minus_kolmrate 		
													
        #################################
        # END REYNOLDS STRESS YY EQUATION 
        #################################  	

        # assign global data to be shared across whole class
        self.data_prefix = data_prefix		
        self.xzn0        = xzn0
        self.dd          = dd
        self.ryy         = ryy		
			
    def plot_ryy(self,LAXIS,xbl,xbr,ybu,ybd,ilg):
        """Plot Reynolds stress yy in the model""" 
		
        # load x GRID
        grd1 = self.xzn0
	
        # load DATA to plot 		
        plt1 = self.ryy
		
        # create FIGURE
        plt.figure(figsize=(7,6))
		
        # format AXIS, make sure it is exponential
        plt.gca().yaxis.get_major_formatter().set_powerlimits((0,0))		
		
        # set plot boundaries   
        to_plot = [plt1]		
        self.set_plt_axis(LAXIS,xbl,xbr,ybu,ybd,to_plot)		
				
        # plot DATA 
        plt.title('ryy')
        plt.plot(grd1,plt1,color='brown',label = r"$\overline{\rho} \widetilde{u''_\theta u''_\theta}$")

        # define and show x/y LABELS
        setxlabel = r"r (cm)"
        setylabel = r"$R_{yy}$ (erg g$^{-1}$)"
        plt.xlabel(setxlabel)
        plt.ylabel(setylabel)
		
        # show LEGEND
        plt.legend(loc=ilg,prop={'size':18})

        # display PLOT
        plt.show(block=False)

        # save PLOT
        plt.savefig('RESULTS/'+self.data_prefix+'mean_ryy.png')		

    def plot_ryy_equation(self,LAXIS,xbl,xbr,ybu,ybd,ilg):
        """Plot Reynolds stress ryy equation in the model""" 
				
        # load x GRID
        grd1 = self.xzn0

        lhs0 = self.minus_dt_ryy
        lhs1 = self.minus_div_fht_ux_ryy 
		
        rhs0 = self.plus_two_ppf_divuyff		
        rhs1 = self.minus_div_two_fkt
        rhs2 = self.minus_two_ryx_grad_fht_uy
        rhs3 = self.plus_two_Gkt
		
        res = self.minus_resRyyEquation
		
        #rhs4 = self.minus_onethrd_kolmrate*self.dd		
		
        # create FIGURE
        plt.figure(figsize=(7,6))
		
        # set plot boundaries   
        to_plot = [lhs0,lhs1,rhs0,rhs1,rhs2,rhs3,res]		
        self.set_plt_axis(LAXIS,xbl,xbr,ybu,ybd,to_plot)		
		
        # format AXIS, make sure it is exponential
        plt.gca().yaxis.get_major_formatter().set_powerlimits((0,0))		
		
        # plot DATA 
        plt.title('reynolds stress yy equation')
        plt.plot(grd1,-lhs0,color='#FF6EB4',label = r'$-\partial_t R_{\theta \theta}$')
        plt.plot(grd1,-lhs1,color='k',label = r"$-\nabla_r (\widetilde{u}_r R_{\theta \theta})$")	
		  
        plt.plot(grd1,rhs0,color='c',label = r"$+2 \overline{P' \nabla u''_\theta }$") 
        plt.plot(grd1,rhs1,color='#802A2A',label = r"$-\nabla_r 2 f_k^t$") 
        plt.plot(grd1,rhs2,color='b',label = r"$-\widetilde{R}_{\theta r}\partial_r \widetilde{u_\theta}$")		
        plt.plot(grd1,rhs3,color='y',label=r"$2 \mathcal{G}_k^t$")
        #plt.plot(grd1,rhs4,color='k',linewidth=0.7,label = r"$-\overline{\rho} 1/3 u^{'3}_{rms}/l_c$")		
        plt.plot(grd1,res,color='k',linestyle='--',label=r"res $\sim N_{Rtt}$")
 
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
        plt.savefig('RESULTS/'+self.data_prefix+'ryy_eq.png')	
	
    def tke_dissipation(self):
        return self.minus_resTkeEquation		

    def tke(self):
        return self.tke		
		
