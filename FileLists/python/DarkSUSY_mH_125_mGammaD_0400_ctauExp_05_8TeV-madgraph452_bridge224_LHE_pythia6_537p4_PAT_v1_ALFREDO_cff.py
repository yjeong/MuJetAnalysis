import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_000.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_001.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_002.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_003.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_004.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_005.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_006.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_007.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_008.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_009.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_010.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_011.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_012.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_013.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_014.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_015.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_016.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_017.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_018.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_019.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_020.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_021.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_022.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_023.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_024.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_025.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_026.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_027.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_028.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_029.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_030.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_031.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_032.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_033.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_034.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_035.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_036.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_037.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_038.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_039.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_040.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_041.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_042.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_043.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_044.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_045.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_046.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_047.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_048.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_049.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_050.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_051.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_052.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_053.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_054.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_055.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_056.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_057.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_058.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_059.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_060.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_061.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_062.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_063.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_064.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_065.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_066.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_067.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_068.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_069.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_070.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_071.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_072.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_073.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_074.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_075.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_076.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_077.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_078.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_079.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_080.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_081.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_082.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_083.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_084.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_085.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_086.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_087.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_088.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_089.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_090.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_091.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_092.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_093.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_094.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_095.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_096.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_097.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_098.root',
    '/store/user/castaned/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/Ntup_099.root',
 ] );


secFiles.extend( [
               ] )
