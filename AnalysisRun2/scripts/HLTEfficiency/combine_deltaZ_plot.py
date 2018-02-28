import sys
from ROOT import *
from argparse import ArgumentParser

from hepPlotter import HepPlotter
import hepPlotterTools as hpt
#import hepPlotterLabels as hpl

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Helpers import *

mass_strings = {
    "0p25": "0.25", 
    "0p275" : "0.275", "0p3": "0.3", "0p4" : "0.4", "0p7" : "0.7", 
    "1" : "1.0", "1p5" : "1.5", "2" : "2.0", "5" : "5.0", "8p5" : "8.5"
}

mass_indices = {
    "0p25": 0, "0p3": 1, "0p4" : 2, "0p7" : 3, "1" : 4, "1p5" : 5, "2" : 6, "5" : 7, "8p5" : 8
}

cT_strings = {
  "0" : 0.0, "0p05" :  0.05, "0p1" :  0.10, "0p2" :  0.20, "0p5" :  0.50, "1" :  1.00, 
  "200" :  2.00, "300" :  3.00, "500" :  5.00, "1000" :  10.0, "2000" :  20.0, "8500" :  85.0
}

cT_strings2 = {
  "0" : "0", "0p05" : "0.05", "0p1" : "0.1", "0p2" : "0.2", "0p5" : "0.50", "1" : "1", 
  "2" : "2", "3" : "3", "5" : "5", "10" : "10", "20" : "20", "50" : "50", "100" : "100"
}

cT_indices = {
  "0" : 0, "0p05" : 1, "0p1" : 2, "0p2" : 3, "0p5" : 4, "1" : 5, 
  "2" : 6 ,  "3" : 7, "5" : 8, "10" : 9, "20" : 10, "50" : 11, "100" : 12
};

mass_colors = {
  "0250", kRed, "0275", kOrange, "0300", kSpring, "0400", kGreen+2, "0700", kAzure+9, 
  "1000", kBlue, "1500", kViolet+6, "2000", kMagenta, "8500", kBlack
}


def makePlotOne(effTuple, format='pdf'):

    ## setup histogram
    hist = HepPlotter("histogram",1)
    hist.x_relative_size = 10
    hist.y_relative_size = 7
    hist.drawEffDist = False    # draw the physics distribution for efficiency (jet_pt for jet trigger)
    #hist.rebin       = 1
    hist.x_label     = effTuple[1]
    hist.y_label     = "Entries"
    hist.format      = format      # file format for saving image
    hist.saveDir     = 'deltaZ_plots_2016DarkSUSY_20180124/'

    n1, ma, ctau  = decodeDarkSUSYFileName(effTuple[2])
    #print n1, ma, ctau
    modified_darkSUSY = getDarkSUSYFileName(n1, ma, ctau)

    #hist.saveAs      = effTuple[2].replace('_13TeV_deltaZ_DiMuonC_DiMuonF','') # save figure with name
    hist.saveAs      = modified_darkSUSY + '_deltaZ_DiMuonC_DiMuonF' # save figure with name
    hist.CMSlabel       = 'outer'  # 'top left', 'top right'; hack code for something else
    hist.CMSlabelStatus = 'Simulation Preliminary'  # ('Simulation')+'Internal' || 'Preliminary' 
    hist.initialize()
    hist.plotLUMI = False
    hist.lumi = '2017 C, XX'
    hist.logplot = True
    hist.yMaxScaleValues = 1.0
    hist.xlim = (-0.5,0.5)
    hist.drawStatUncertainty = True    
    hist.Add(effTuple[0], draw='step', color='blue', 
             linecolor='blue', linestyle='solid',label='')

    hist.extra_text.Add(r"\textbf{Dark SUSY}", coords=[0.1,0.4])
    hist.extra_text.Add(r"$m_{N1} = %s~\mathrm{GeV}$"%n1, coords=[0.1,0.35])
    hist.extra_text.Add(r"$m_{\gamma D} = %s~\mathrm{GeV}$"%(mass_strings[ma]), coords=[0.1,0.3])
    hist.extra_text.Add(r"$c_{\tau} = %s~\mathrm{mm}$"%cT_strings2[ctau], coords=[0.1,0.25])
    plot = hist.execute()
    hist.savefig()


def makePlot(effTuple, format='pdf'):

    ## setup histogram
    hist = HepPlotter("histogram",1)
    hist.x_relative_size = 10
    hist.y_relative_size = 7
    hist.drawEffDist = False    # draw the physics distribution for efficiency (jet_pt for jet trigger)
    #hist.rebin       = 1
    hist.x_label     = effTuple[1]
    hist.y_label     = "Entries"
    hist.format      = format      # file format for saving image
    hist.saveDir     = 'deltaZ_plots_2016DarkSUSY_20180124/'

    n1, ma, ctau  = decodeDarkSUSYFileName(effTuple[2])
    #print n1, ma, ctau
    modified_darkSUSY = getDarkSUSYFileNameNoCT(n1, ma)

    #hist.saveAs      = effTuple[2].replace('_13TeV_deltaZ_DiMuonC_DiMuonF','') # save figure with name
    hist.saveAs      = modified_darkSUSY + '_deltaZ_DiMuonC_DiMuonF' # save figure with name
    hist.CMSlabel       = 'outer'  # 'top left', 'top right'; hack code for something else
    hist.CMSlabelStatus = 'Simulation Preliminary'  # ('Simulation')+'Internal' || 'Preliminary' 
    hist.initialize()
    hist.plotLUMI = False
    hist.lumi = '2017 C, XX'
    hist.logplot = True
    hist.yMaxScaleValues = 1.0
    hist.xlim = (-0.5,0.5)
    hist.drawStatUncertainty = True    
    hist.Add(effTuple[0], draw='step', color='blue', 
             linecolor='blue', linestyle='solid',label='')

    hist.extra_text.Add(r"\textbf{Dark SUSY}", coords=[0.1,0.4])
    hist.extra_text.Add(r"$m_{N1} = %s~\mathrm{GeV}$"%n1, coords=[0.1,0.35])
    hist.extra_text.Add(r"$m_{\gamma D} = %s~\mathrm{GeV}$"%(mass_strings[ma]), coords=[0.1,0.3])
    #hist.extra_text.Add(r"$c_{\tau} = %s~\mathrm{mm}$"%cT_strings2[ctau], coords=[0.1,0.25])
    plot = hist.execute()
    hist.savefig()


def makePlotAll(effTuple, format='pdf'):

    ## setup histogram
    hist = HepPlotter("histogram",1)
    hist.x_relative_size = 10
    hist.y_relative_size = 7
    hist.drawEffDist = False    # draw the physics distribution for efficiency (jet_pt for jet trigger)
    #hist.rebin       = 1
    hist.x_label     = effTuple[1]
    hist.y_label     = "Entries"
    hist.format      = format      # file format for saving image
    hist.saveDir     = 'deltaZ_plots_2016DarkSUSY_20180124/'
    #hist.saveAs      = effTuple[2].replace('_13TeV_deltaZ_DiMuonC_DiMuonF','') # save figure with name
    hist.saveAs      = effTuple[2] + '_deltaZ_DiMuonC_DiMuonF' # save figure with name
    hist.CMSlabel       = 'outer'  # 'top left', 'top right'; hack code for something else
    hist.CMSlabelStatus = 'Simulation Preliminary'  # ('Simulation')+'Internal' || 'Preliminary' 
    hist.initialize()
    hist.plotLUMI = False
    hist.logplot = True
    hist.yMaxScaleValues = 1.0
    hist.xlim = (-0.5,0.5)
    hist.lumi = '2017 C, XX'
    hist.drawStatUncertainty = True    
    hist.Add(effTuple[0], draw='step', color='blue', 
             linecolor='blue', linestyle='solid',label='')

    hist.extra_text.Add(r"\textbf{Dark SUSY}", coords=[0.1,0.4])
    hist.extra_text.Add(r"$m_{N1} = 10~\mathrm{GeV}$", coords=[0.1,0.35])
    hist.extra_text.Add(r"$m_{\gamma D} = 2.5-8.5~\mathrm{GeV}$", coords=[0.1,0.3])
    hist.extra_text.Add(r"$c_{\tau} = 0-100\mathrm{mm}$", coords=[0.1,0.25])
    plot = hist.execute()
    hist.savefig()


## make plots
deltaZ_2016MonteCarlo = {}

DarkSUSY_mH_125_mN1_10_mGammaD_0p25 = [
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p25_cT_0_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p25_cT_0p05_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p25_cT_0p1_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p25_cT_0p5_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p25_cT_1_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p25_cT_2_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p25_cT_5_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p25_cT_10_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p25_cT_20_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p25_cT_50_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p25_cT_100_13TeV_deltaZ_DiMuonC_DiMuonF',
]
DarkSUSY_mH_125_mN1_10_mGammaD_0p3 = [
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p3_cT_0p05_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p3_cT_0p2_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p3_cT_3_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p3_cT_50_13TeV_deltaZ_DiMuonC_DiMuonF',
]
DarkSUSY_mH_125_mN1_10_mGammaD_0p4 = [
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p4_cT_0_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p4_cT_0p05_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p4_cT_0p1_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p4_cT_0p5_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p4_cT_1_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p4_cT_2_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p4_cT_3_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p4_cT_10_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p4_cT_20_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p4_cT_50_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p4_cT_100_13TeV_deltaZ_DiMuonC_DiMuonF',
    ]
DarkSUSY_mH_125_mN1_10_mGammaD_0p7 = [
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p7_cT_0_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p7_cT_0p05_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p7_cT_0p1_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p7_cT_0p2_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p7_cT_0p5_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p7_cT_1_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p7_cT_3_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p7_cT_10_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p7_cT_20_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p7_cT_50_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p7_cT_100_13TeV_deltaZ_DiMuonC_DiMuonF',
    ]
DarkSUSY_mH_125_mN1_10_mGammaD_1 = [
    'DarkSUSY_mH_125_mN1_10_mGammaD_1_cT_0_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_1_cT_3_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_1_cT_5_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_1_cT_10_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_1_cT_20_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_1_cT_50_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_1_cT_100_13TeV_deltaZ_DiMuonC_DiMuonF',
    ]
DarkSUSY_mH_125_mN1_10_mGammaD_1p5 = [
    'DarkSUSY_mH_125_mN1_10_mGammaD_1p5_cT_3_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_1p5_cT_10_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_1p5_cT_50_13TeV_deltaZ_DiMuonC_DiMuonF',
    ]
DarkSUSY_mH_125_mN1_10_mGammaD_2 = [
    'DarkSUSY_mH_125_mN1_10_mGammaD_2_cT_10_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_2_cT_50_13TeV_deltaZ_DiMuonC_DiMuonF',
    ]
DarkSUSY_mH_125_mN1_10_mGammaD_5 = [
    'DarkSUSY_mH_125_mN1_10_mGammaD_5_cT_0_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_5_cT_3_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_5_cT_10_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_5_cT_20_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_5_cT_50_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_5_cT_100_13TeV_deltaZ_DiMuonC_DiMuonF',
    ]
DarkSUSY_mH_125_mN1_10_mGammaD_8p5 = [
    'DarkSUSY_mH_125_mN1_10_mGammaD_8p5_cT_0_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_8p5_cT_2_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_8p5_cT_3_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_8p5_cT_10_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_8p5_cT_20_13TeV_deltaZ_DiMuonC_DiMuonF',
    'DarkSUSY_mH_125_mN1_10_mGammaD_8p5_cT_50_13TeV_deltaZ_DiMuonC_DiMuonF',
    ]

DarkSUSY_mH_125_mN1_10 = {
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p25' : DarkSUSY_mH_125_mN1_10_mGammaD_0p25,
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p3' :  DarkSUSY_mH_125_mN1_10_mGammaD_0p3,
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p4' :  DarkSUSY_mH_125_mN1_10_mGammaD_0p4,
    'DarkSUSY_mH_125_mN1_10_mGammaD_0p7' :  DarkSUSY_mH_125_mN1_10_mGammaD_0p7,
    'DarkSUSY_mH_125_mN1_10_mGammaD_1' :    DarkSUSY_mH_125_mN1_10_mGammaD_1,
    'DarkSUSY_mH_125_mN1_10_mGammaD_1p5' :  DarkSUSY_mH_125_mN1_10_mGammaD_1p5,
    'DarkSUSY_mH_125_mN1_10_mGammaD_2' :    DarkSUSY_mH_125_mN1_10_mGammaD_2,
    'DarkSUSY_mH_125_mN1_10_mGammaD_5' :    DarkSUSY_mH_125_mN1_10_mGammaD_5,
    'DarkSUSY_mH_125_mN1_10_mGammaD_8p5' :  DarkSUSY_mH_125_mN1_10_mGammaD_8p5,
    }

MyFile = TFile("deltaZ_DiMuonC_DiMuonF_2016.root");


deltaZCut = 0.1

firstAll = True
for p in DarkSUSY_mH_125_mN1_10:
    print "Checking", p
    first = True

    for q in DarkSUSY_mH_125_mN1_10[p]:
        print q,
        deltaZ_2016MonteCarlo[q] = MyFile.Get(q)
        print deltaZ_2016MonteCarlo[q].Integral(deltaZ_2016MonteCarlo[q].GetXaxis().FindBin(-deltaZCut), 
                                                deltaZ_2016MonteCarlo[q].GetXaxis().FindBin(deltaZCut))*1./deltaZ_2016MonteCarlo[q].Integral(0,3000), deltaZ_2016MonteCarlo[q].Integral(0,3000)
        #makePlotOne((deltaZ_2016MonteCarlo[q], 
        #             r"$\Delta z(\mu\mu_1,\mu\mu_2)$", q), format='pdf')

        if first:
            deltaZ_2016MonteCarlo[p] = deltaZ_2016MonteCarlo[q]
            first = False
        else:
            deltaZ_2016MonteCarlo[p].Add(deltaZ_2016MonteCarlo[q])
        
        if firstAll:
            deltaZ_2016MonteCarlo["DarkSUSY_mH_125_mN1_10"] = deltaZ_2016MonteCarlo[q]
            firstAll = False
        else:
            deltaZ_2016MonteCarlo["DarkSUSY_mH_125_mN1_10"].Add(deltaZ_2016MonteCarlo[q])

    print "RMS", p, deltaZ_2016MonteCarlo[p].GetRMS(), deltaZ_2016MonteCarlo[p].GetRMSError()
    # need ctau to make the deocde function work!
    # even though it is not used to make the plot
    #makePlot((deltaZ_2016MonteCarlo[p], 
    #          r"$\Delta z(\mu\mu_1,\mu\mu_2)$", DarkSUSY_mH_125_mN1_10[p][0]), format='pdf')

print "All combined", deltaZ_2016MonteCarlo["DarkSUSY_mH_125_mN1_10"].Integral(deltaZ_2016MonteCarlo["DarkSUSY_mH_125_mN1_10"].GetXaxis().FindBin(-deltaZCut),
                                                                               deltaZ_2016MonteCarlo["DarkSUSY_mH_125_mN1_10"].GetXaxis().FindBin(deltaZCut))*1./deltaZ_2016MonteCarlo["DarkSUSY_mH_125_mN1_10"].Integral(0,3000), deltaZ_2016MonteCarlo["DarkSUSY_mH_125_mN1_10"].Integral(0,3000)
#makePlotAll((deltaZ_2016MonteCarlo["DarkSUSY_mH_125_mN1_10"], 
#             r"$\Delta z(\mu\mu_1,\mu\mu_2)$", "DarkSUSY_mH_125_mN1_10"), format='pdf')

MyFile.Close()


## plot of the RMS versus dark photon mass
#for p in DarkSUSY_mH_125_mN1_10:
#    print "RMS", p, deltaZ_2016MonteCarlo[p].GetRMS()



def makePlotRMS(effTuple, format='pdf'):

    ## setup histogram
    hist = HepPlotter("histogram",1)
    hist.x_relative_size = 10
    hist.y_relative_size = 7
    hist.drawEffDist = False    # draw the physics distribution for efficiency (jet_pt for jet trigger)
    #hist.rebin       = 1
    hist.x_label     = effTuple[1]
    hist.y_label     = "RMS [GeV]"
    hist.format      = format      # file format for saving image
    hist.saveDir     = 'deltaZ_plots_2016DarkSUSY_20180124/'

    #hist.saveAs      = effTuple[2].replace('_13TeV_deltaZ_DiMuonC_DiMuonF','') # save figure with name
    hist.saveAs      = 'DarkSUSY_mH_125_mN1_10_deltaZ_DiMuonC_DiMuonF_RMS' # save figure with name
    hist.CMSlabel       = 'outer'  # 'top left', 'top right'; hack code for something else
    hist.CMSlabelStatus = 'Simulation Preliminary'  # ('Simulation')+'Internal' || 'Preliminary' 
    hist.initialize()
    hist.plotLUMI = False
    hist.lumi = '2017 C, XX'
    hist.ymaxScale = 1.0
    hist.drawStatUncertainty = True    
    hist.Add(effTuple[0], draw='step', color='blue', 
             linecolor='blue', linestyle='solid',label='')

    hist.extra_text.Add(r"\textbf{Dark SUSY}", coords=[0.1,0.4])
    hist.extra_text.Add(r"$m_{N1} = 10~\mathrm{GeV}$", coords=[0.1,0.35])
    hist.extra_text.Add(r"$m_{\gamma D} = 0.25-8.5\mathrm{GeV}$", coords=[0.1,0.3])
    #hist.extra_text.Add(r"$c_{\tau} = %s~\mathrm{mm}$"%cT_strings2[ctau], coords=[0.1,0.25])
    plot = hist.execute()
    hist.savefig()



darkSUSYMass_RMS = TH1D("darkSUSYMass_RMS","; dark photon mass [GeV]; RMS [GeV]",9,0,9)
darkSUSYMass_RMS.GetXaxis().SetBinLabel(1,"0.25")
darkSUSYMass_RMS.GetXaxis().SetBinLabel(2,"0.3")
darkSUSYMass_RMS.GetXaxis().SetBinLabel(3,"0.4")
darkSUSYMass_RMS.GetXaxis().SetBinLabel(4,"0.7")
darkSUSYMass_RMS.GetXaxis().SetBinLabel(5,"1")
darkSUSYMass_RMS.GetXaxis().SetBinLabel(6,"1.5")
darkSUSYMass_RMS.GetXaxis().SetBinLabel(7,"2")
darkSUSYMass_RMS.GetXaxis().SetBinLabel(8,"5")
darkSUSYMass_RMS.GetXaxis().SetBinLabel(9,"8.5")

darkSUSYMass_RMS.SetBinContent(1,0.0186297882103)
darkSUSYMass_RMS.SetBinContent(2,0.0110012356382)
darkSUSYMass_RMS.SetBinContent(3,0.0210072881979)
darkSUSYMass_RMS.SetBinContent(4,0.0227770520789)
darkSUSYMass_RMS.SetBinContent(5,0.0277416364169)
darkSUSYMass_RMS.SetBinContent(6,0.0425292718721)
darkSUSYMass_RMS.SetBinContent(7,0.0503304051597)
darkSUSYMass_RMS.SetBinContent(8,0.0831847843198)
darkSUSYMass_RMS.SetBinContent(9,0.0866813088559)

canvas = TCanvas("canvas","",800,600)
canvas.cd()
darkSUSYMass_RMS.Draw()
canvas.SaveAs("deltaZ_plots_2016DarkSUSY_20180124/DarkSUSY_mH_125_mN1_10_deltaZ_DiMuonC_DiMuonF_RMS.pdf")
#makePlotRMS((darkSUSYMass_RMS,"dark photon mass [GeV]"))