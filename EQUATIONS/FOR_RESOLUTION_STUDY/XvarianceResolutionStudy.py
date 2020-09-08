import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import UTILS.Calculus as calc
import UTILS.SetAxisLimit as al
import UTILS.Tools as uT
import UTILS.Errors as eR
import sys

# Theoretical background https://arxiv.org/abs/1401.5176

# Mocak, Meakin, Viallet, Arnett, 2014, Compressible Hydrodynamic Mean-Field #
# Equations in Spherical Geometry and their Application to Turbulent Stellar #
# Convection Data #

class XvarianceResolutionStudy(calc.Calculus, al.SetAxisLimit, uT.Tools, eR.Errors, object):

    def __init__(self, filename, ig, inuc, element, intc, data_prefix):
        super(XvarianceResolutionStudy, self).__init__(ig)

        # load data to list of structured arrays
        eht = []
        for ffile in filename:
            eht.append(np.load(ffile))

        # declare data lists		
        xzn0, nx, ny, nz = [], [], [], []

        timec, sigmai = [], []

        for i in range(len(filename)):
            # load time
            timec.append(np.asarray(eht[i].item().get('timec')[intc]))
            # load grid
            xzn0.append(np.asarray(eht[i].item().get('xzn0')))

            nx.append(np.asarray(eht[i].item().get('nx')))
            ny.append(np.asarray(eht[i].item().get('ny')))
            nz.append(np.asarray(eht[i].item().get('nz')))

            dd = np.asarray(eht[i].item().get('dd')[intc])
            ddux = np.asarray(eht[i].item().get('ddux')[intc])
            ddxi = np.asarray(eht[i].item().get('ddx' + inuc)[intc])
            ddxisq = np.asarray(eht[i].item().get('ddx' + inuc + 'sq')[intc])

            xivar = (ddxisq - ddxi * ddxi / dd) / dd

            sigmai.append(xivar)

        # share data globally
        self.data_prefix = data_prefix
        self.xzn0 = xzn0
        self.inuc = inuc
        self.element = element
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.sigmai = sigmai
        self.ig = ig
        self.timec = timec

    def plot_Xvariance(self, LAXIS, xbl, xbr, ybu, ybd, ilg):
        """Plot composition variance in the model"""

        # load x GRID
        grd = self.xzn0

        # load DATA to plot		
        plt1 = self.sigmai
        nx = self.nx
        ny = self.ny
        nz = self.nz

        # find maximum resolution data
        grd_maxres = self.maxresdata(grd)
        plt1_maxres = self.maxresdata(plt1)

        plt_interp = []
        for i in range(len(grd)):
            plt_interp.append(np.interp(grd_maxres, grd[i], plt1[i]))

        # create FIGURE
        plt.figure(figsize=(7, 6))

        # format AXIS, make sure it is exponential
        plt.gca().yaxis.get_major_formatter().set_powerlimits((0, 0))

        plt10_tmp = plt1[0]
        plt11_tmp = plt1[0]

        plt1_foraxislimit = []
        plt1max = np.max(plt1[0])
        for plt1i in plt1:
            if (np.max(plt1i) > plt1max):
                plt1_foraxislimit = plt1i

        # set plot boundaries
        to_plot = [plt1_foraxislimit]
        self.set_plt_axis(LAXIS, xbl, xbr, ybu, ybd, to_plot)

        # plot DATA 
        plt.title('Xvariance for ' + self.element)

        for i in range(len(grd)):
            plt.plot(grd[i], plt1[i], label=str(self.nx[i]) + ' x ' + str(self.ny[i]) + ' x ' + str(self.nz[i]) +
                                            ' t: ' + str(round(self.timec[i])) + ' s')

        # define and show x/y LABELS
        if self.ig == 1:
            setxlabel = r"x (cm)"
            setylabel = r"$\sigma_i$"
            plt.xlabel(setxlabel)
            plt.ylabel(setylabel)
        elif self.ig == 2:
            setxlabel = r"r (cm)"
            setylabel = r"$\sigma_i$"
            plt.xlabel(setxlabel)
            plt.ylabel(setylabel)

        # show LEGEND
        plt.legend(loc=ilg, prop={'size': 14})

        # display PLOT
        plt.show(block=False)

        # save PLOT
        plt.savefig('RESULTS/' + self.data_prefix + 'mean_Xvariance_' + self.element + '.png')

    # find data with maximum resolution	
    def maxresdata(self, data):
        tmp = 0
        for idata in data:
            if idata.shape[0] > tmp:
                data_maxres = idata
            else:
                tmp = idata.shape[0]

        return data_maxres
