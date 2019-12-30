import FOURIER.FOR_RESOLUTION_STUDY.SpectrumTurbulentKineticEnergyResolutionStudy as stke
import FOURIER.FOR_RESOLUTION_STUDY.SpectrumUxVarianceResolutionStudy as suxv
import FOURIER.FOR_RESOLUTION_STUDY.SpectrumUyVarianceResolutionStudy as suyv
import FOURIER.FOR_RESOLUTION_STUDY.SpectrumUzVarianceResolutionStudy as suzv
import FOURIER.FOR_RESOLUTION_STUDY.SpectrumDensityVarianceResolutionStudy as sddv
import FOURIER.FOR_RESOLUTION_STUDY.SpectrumPressureVarianceResolutionStudy as sppv
import FOURIER.FOR_RESOLUTION_STUDY.SpectrumTemperatureVarianceResolutionStudy as sttv
import FOURIER.FOR_RESOLUTION_STUDY.SpectrumTotalEnergyVarianceResolutionStudy as setv
import FOURIER.FOR_RESOLUTION_STUDY.SpectrumXcompositionVarianceResolutionStudy as sxrhov

import matplotlib.pyplot as plt


class ResFourierMasterPlot():

    def __init__(self, params):
        self.params = params

    def execFourierTKE(self):
        params = self.params

        # instantiate 		
        fourierTKE = \
            stke.SpectrumTurbulentKineticEnergyResolutionStudy( \
                params.getForProp('fourier')['datadir'], \
                params.getForProp('fourier')['datafiles'], \
                params.getForProp('fourier')['prefix'], \
                params.getForProp('fourier')['ig'], \
                params.getForProp('fourier')['lhc'])

        # plot    
        fourierTKE.plot_TKEspectrum(params.getForProp('fourier')['laxis'], \
                                    params.getForEqs('fstke')['xbl'], \
                                    params.getForEqs('fstke')['xbr'], \
                                    params.getForEqs('fstke')['ybu'], \
                                    params.getForEqs('fstke')['ybd'], \
                                    params.getForEqs('fstke')['ilg'])

    def execFourierUx(self):
        params = self.params

        # instantiate
        fourierUX = \
            suxv.SpectrumUxVarianceResolutionStudy( \
                params.getForProp('fourier')['datadir'], \
                params.getForProp('fourier')['datafiles'], \
                params.getForProp('fourier')['prefix'], \
                params.getForProp('fourier')['ig'], \
                params.getForProp('fourier')['lhc'])

        # plot
        fourierUX.plot_UXspectrum(params.getForProp('fourier')['laxis'], \
                                  params.getForEqs('fsux')['xbl'], \
                                  params.getForEqs('fsux')['xbr'], \
                                  params.getForEqs('fsux')['ybu'], \
                                  params.getForEqs('fsux')['ybd'], \
                                  params.getForEqs('fsux')['ilg'])

    def execFourierUy(self):
        params = self.params

        # instantiate
        fourierUY = \
            suyv.SpectrumUyVarianceResolutionStudy( \
                params.getForProp('fourier')['datadir'], \
                params.getForProp('fourier')['datafiles'], \
                params.getForProp('fourier')['prefix'], \
                params.getForProp('fourier')['ig'], \
                params.getForProp('fourier')['lhc'])

        # plot
        fourierUY.plot_UYspectrum(params.getForProp('fourier')['laxis'], \
                                  params.getForEqs('fsuy')['xbl'], \
                                  params.getForEqs('fsuy')['xbr'], \
                                  params.getForEqs('fsuy')['ybu'], \
                                  params.getForEqs('fsuy')['ybd'], \
                                  params.getForEqs('fsuy')['ilg'])

    def execFourierUz(self):
        params = self.params

        # instantiate
        fourierUZ = \
            suzv.SpectrumUzVarianceResolutionStudy( \
                params.getForProp('fourier')['datadir'], \
                params.getForProp('fourier')['datafiles'], \
                params.getForProp('fourier')['prefix'], \
                params.getForProp('fourier')['ig'], \
                params.getForProp('fourier')['lhc'])

        # plot
        fourierUZ.plot_UZspectrum(params.getForProp('fourier')['laxis'], \
                                  params.getForEqs('fsuz')['xbl'], \
                                  params.getForEqs('fsuz')['xbr'], \
                                  params.getForEqs('fsuz')['ybu'], \
                                  params.getForEqs('fsuz')['ybd'], \
                                  params.getForEqs('fsuz')['ilg'])

    def execFourierDD(self):
        params = self.params

        # instantiate
        fourierDD = \
            sddv.SpectrumDensityVarianceResolutionStudy( \
                params.getForProp('fourier')['datadir'], \
                params.getForProp('fourier')['datafiles'], \
                params.getForProp('fourier')['prefix'], \
                params.getForProp('fourier')['ig'], \
                params.getForProp('fourier')['lhc'])

        # plot
        fourierDD.plot_DDspectrum(params.getForProp('fourier')['laxis'], \
                                  params.getForEqs('fsdd')['xbl'], \
                                  params.getForEqs('fsdd')['xbr'], \
                                  params.getForEqs('fsdd')['ybu'], \
                                  params.getForEqs('fsdd')['ybd'], \
                                  params.getForEqs('fsdd')['ilg'])


    def execFourierPP(self):
        params = self.params

        # instantiate
        fourierPP = \
            sppv.SpectrumPressureVarianceResolutionStudy( \
                params.getForProp('fourier')['datadir'], \
                params.getForProp('fourier')['datafiles'], \
                params.getForProp('fourier')['prefix'], \
                params.getForProp('fourier')['ig'], \
                params.getForProp('fourier')['lhc'])

        # plot
        fourierPP.plot_PPspectrum(params.getForProp('fourier')['laxis'], \
                                  params.getForEqs('fspp')['xbl'], \
                                  params.getForEqs('fspp')['xbr'], \
                                  params.getForEqs('fspp')['ybu'], \
                                  params.getForEqs('fspp')['ybd'], \
                                  params.getForEqs('fspp')['ilg'])

    def execFourierTT(self):
        params = self.params

        # instantiate
        fourierTT = \
            sttv.SpectrumTemperatureVarianceResolutionStudy( \
                params.getForProp('fourier')['datadir'], \
                params.getForProp('fourier')['datafiles'], \
                params.getForProp('fourier')['prefix'], \
                params.getForProp('fourier')['ig'], \
                params.getForProp('fourier')['lhc'])

        # plot
        fourierTT.plot_TTspectrum(params.getForProp('fourier')['laxis'], \
                                  params.getForEqs('fstt')['xbl'], \
                                  params.getForEqs('fstt')['xbr'], \
                                  params.getForEqs('fstt')['ybu'], \
                                  params.getForEqs('fstt')['ybd'], \
                                  params.getForEqs('fstt')['ilg'])

    def execFourierET(self):
        params = self.params

        # instantiate
        fourierET = \
            setv.SpectrumTotalEnergyVarianceResolutionStudy( \
                params.getForProp('fourier')['datadir'], \
                params.getForProp('fourier')['datafiles'], \
                params.getForProp('fourier')['prefix'], \
                params.getForProp('fourier')['ig'], \
                params.getForProp('fourier')['lhc'])

        # plot
        fourierET.plot_ETspectrum(params.getForProp('fourier')['laxis'], \
                                  params.getForEqs('fset')['xbl'], \
                                  params.getForEqs('fset')['xbr'], \
                                  params.getForEqs('fset')['ybu'], \
                                  params.getForEqs('fset')['ybd'], \
                                  params.getForEqs('fset')['ilg'])

    def execFourierXrho(self, inuc, element, x):
        params = self.params

        # instantiate
        fourierXrho = sxrhov.SpectrumXcompositionVarianceResolutionStudy( \
                                                          params.getForProp('fourier')['datadir'], \
                                                          params.getForProp('fourier')['datafiles'], \
                                                          params.getForProp('fourier')['prefix'], \
                                                          params.getForProp('fourier')['ig'], \
                                                          params.getForProp('fourier')['lhc'], inuc, element)

        fourierXrho.plot_XrhoSpectrum(params.getForProp('fourier')['laxis'], \
                                      params.getForEqs(x)['xbl'], \
                                      params.getForEqs(x)['xbr'], \
                                      params.getForEqs(x)['ybu'], \
                                      params.getForEqs(x)['ybd'], \
                                      params.getForEqs(x)['ilg'])


    def SetMatplotlibParams(self):
        """ This routine sets some standard values for matplotlib """
        """ to obtain publication-quality figures """

        # plt.rc('text',usetex=True)
        # plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
        plt.rc('font', **{'family': 'serif', 'serif': ['Times New Roman']})
        plt.rc('font', size=16.)
        plt.rc('lines', linewidth=2, markeredgewidth=2., markersize=12)
        plt.rc('axes', linewidth=1.5)
        plt.rcParams['xtick.major.size'] = 8.
        plt.rcParams['xtick.minor.size'] = 4.
        plt.rcParams['figure.subplot.bottom'] = 0.15
        plt.rcParams['figure.subplot.left'] = 0.17
        plt.rcParams['figure.subplot.right'] = 0.85
        plt.rcParams.update({'figure.max_open_warning': 0})