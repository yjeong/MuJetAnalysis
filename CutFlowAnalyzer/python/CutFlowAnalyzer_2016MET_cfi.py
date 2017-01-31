import FWCore.ParameterSet.Config as cms

cutFlowAnalyzer = cms.EDAnalyzer('CutFlowAnalyzer_AOD',
    analyzerDebug = cms.int32(0),
    fillGenLevel = cms.bool(True),
#    muons = cms.InputTag("cleanPatTrackerMuonsTriggerMatch"),
#    muJets = cms.InputTag("TrackerMuJetProducer05"),
    muons = cms.InputTag("cleanPatPFMuonsTriggerMatch"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    muJets = cms.InputTag("PFMuJetProducer05"),
    muJetOrphans = cms.InputTag("PFMuJetProducer05", "Orphans"),
    tracks = cms.InputTag("generalTracks"),
                                 triggerEvent = cms.InputTag("patTriggerEvent"),
    TriggerResults = cms.InputTag("TriggerResults","","HLT"),
    TrackRefitter = cms.InputTag("TrackRefitter"),
    genParticles = cms.InputTag("genParticles"),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    DiMuons_Iso_Max = cms.double(2.0),
    nThrowsConsistentVertexesCalculator = cms.int32(0),
    barrelPixelLayer = cms.int32(1),
    endcapPixelLayer = cms.int32(1),
    runDisplacedVtxFinder = cms.bool(False),
    runPixelHitRecovery = cms.bool(False),
    Traj = cms.InputTag("TrackRefitter"),
    NavigationSchool   = cms.string('SimpleNavigationSchool'),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag('MeasurementTrackerEvent'),
    Propagator = cms.string("RungeKuttaTrackerPropagator"),
    runBBestimation = cms.bool(True),
    skimOutput = cms.bool(False),
    signalHltPaths = cms.vstring(

        ## only pure-MET triggers
        ##/dev/CMSSW_8_0_0/HLT/V176
        'HLT_MET100_v1',
        'HLT_MET150_v1',
        'HLT_MET200_v1',
        'HLT_MET250_v1',
        'HLT_MET300_v1',
        'HLT_MET600_v1',
        'HLT_MET700_v1',
        'HLT_PFMET100_PFMHT100_IDTight_v2',
        'HLT_PFMET110_PFMHT110_IDTight_v2',
        'HLT_PFMET120_PFMHT120_IDTight_v2',
        'HLT_PFMET170_HBHECleaned_v2',
        'HLT_PFMET170_JetIdCleaned_v2',
        'HLT_PFMET170_NoiseCleaned_v3',
        'HLT_PFMET170_NotCleaned_v1',
        'HLT_PFMET300_v1',
        'HLT_PFMET400_v1',
        'HLT_PFMET500_v1',
        'HLT_PFMET600_v1',
        'HLT_PFMET90_PFMHT90_IDTight_v2',
                                 
        ##/dev/CMSSW_8_0_0/HLT/V185
        ##/dev/CMSSW_8_0_0/HLT/V187
        ##/dev/CMSSW_8_0_0/HLT/V188
        
        ##/dev/CMSSW_8_0_0/HLT/V298
        ##/dev/CMSSW_8_0_0/HLT/V299
        ##/dev/CMSSW_8_0_0/HLT/V300
        
        ##/dev/CMSSW_8_0_0/HLT/V326
        ##/dev/CMSSW_8_0_0/HLT/V327
        ##/dev/CMSSW_8_0_0/HLT/V328
        
        ##/dev/CMSSW_8_0_0/HLT/V365
        ##/dev/CMSSW_8_0_0/HLT/V381
        ##/dev/CMSSW_8_0_0/HLT/V385
        
        ##/dev/CMSSW_8_0_0/HLT/V420
        ##/dev/CMSSW_8_0_0/HLT/V421
        
        ##/dev/CMSSW_8_0_0/HLT/V448
        ##/dev/CMSSW_8_0_0/HLT/V450
        ##/dev/CMSSW_8_0_0/HLT/V453
        
        ##/dev/CMSSW_8_0_0/HLT/V519
        ##/dev/CMSSW_8_0_0/HLT/V531
        ##/dev/CMSSW_8_0_0/HLT/V532
        ##/dev/CMSSW_8_0_0/HLT/V533
        ##/dev/CMSSW_8_0_0/HLT/V536
        ##/dev/CMSSW_8_0_0/HLT/V548
        
        ##/dev/CMSSW_8_0_0/HLT/V538
        ##/dev/CMSSW_8_0_0/HLT/V539
        ##/dev/CMSSW_8_0_0/HLT/V549
        ##/dev/CMSSW_8_0_0/HLT/V550
        ##/dev/CMSSW_8_0_0/HLT/V551
        ##/dev/CMSSW_8_0_0/HLT/V564
        
        ##/dev/CMSSW_8_0_0/HLT/V609
        ##/dev/CMSSW_8_0_0/HLT/V611
        ##/dev/CMSSW_8_0_0/HLT/V613
        ##/dev/CMSSW_8_0_0/HLT/V615
        'HLT_MET100_v3',
        'HLT_MET150_v3',
        'HLT_MET200_v5',
        'HLT_MET250_v5',
        'HLT_MET300_v5',
        'HLT_MET600_v5',
        'HLT_MET700_v5',
        'HLT_PFMET110_PFMHT110_IDTight_v8',
        'HLT_PFMET120_PFMHT120_IDTight_v8',
        'HLT_PFMET170_BeamHaloCleaned_v7',
        'HLT_PFMET170_HBHECleaned_v9',
        'HLT_PFMET170_HBHE_BeamHaloCleaned_v5',
        'HLT_PFMET170_JetIdCleaned_v8',
        'HLT_PFMET170_NoiseCleaned_v9',
        'HLT_PFMET170_NotCleaned_v8',
        'HLT_PFMET300_v7',
        'HLT_PFMET400_v7',
        'HLT_PFMET500_v7',
        'HLT_PFMET600_v7',
        'HLT_PFMETTypeOne190_HBHE_BeamHaloCleaned_v5'
    ),
    backupHltPaths = cms.vstring(
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v1',
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v2',
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v3',
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v4',
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v5',
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v6',
    ),
    otherMuHltPaths = cms.vstring(
        'HLT_DoubleMu18NoFiltersNoVtx_v3',
        'HLT_DoubleMu23NoFiltersNoVtxDisplaced_v3',
        'HLT_DoubleMu28NoFiltersNoVtxDisplaced_v3',
        'HLT_DoubleMu33NoFiltersNoVtx_v3',
        'HLT_DoubleMu38NoFiltersNoVtx_v3',
        'HLT_DoubleMu8_Mass8_PFHT250_v2',
        'HLT_DoubleMu8_Mass8_PFHT300_v5',
        'HLT_L2DoubleMu23_NoVertex_v3',
        'HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10_v3',
        'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_Mass10_v3',
        'HLT_Mu10_CentralPFJet30_BTagCSV_p13_v2',
        'HLT_Mu17_Mu8_DZ_v3',
        'HLT_Mu17_Mu8_SameSign_DZ_v2',
        'HLT_Mu17_Mu8_SameSign_v2',
        'HLT_Mu17_Mu8_v2',
        'HLT_Mu17_TkMu8_DZ_v3',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v3',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v3',
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v3',
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v3',
        'HLT_Mu17_TrkIsoVVL_v3',
        'HLT_Mu17_v3',
        'HLT_Mu20_Mu10_DZ_v2',
        'HLT_Mu20_Mu10_SameSign_DZ_v2',
        'HLT_Mu20_Mu10_SameSign_v1',
        'HLT_Mu20_Mu10_v2',
        'HLT_Mu27_TkMu8_v3',
        'HLT_Mu30_TkMu11_v3',
        'HLT_Mu3_PFJet40_v2',
        'HLT_Mu40_TkMu11_v3',
        'HLT_Mu8_TrkIsoVVL_v4',
        'HLT_Mu8_v4',
        'HLT_TripleMu_12_10_5_v3',
        'HLT_TripleMu_5_3_3_v1',
    )
)
