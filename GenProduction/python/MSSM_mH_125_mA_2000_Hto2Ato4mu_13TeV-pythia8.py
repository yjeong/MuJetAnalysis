# Auto generated configuration file
# using: 
# Revision: 1.381.2.13 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/EightTeV/MSSM_mH_125_mA_2000_Hto2Ato4mu_8TeV-pythia6_cfi.py --step GEN --datatier GEN --conditions auto:startup --eventcontent RECOSIM --python_filename=MSSM_mH_125_mA_2000_Hto2Ato4mu_8TeV-pythia6_537p4_GEN.py --fileout=MSSM_mH_125_mA_2000_Hto2Ato4mu_8TeV-pythia6_537p4_GEN.root -n 10 --no_exec
import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *


process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
	input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
	version = cms.untracked.string('$Revision: 1.381.2.13 $'),
	annotation = cms.untracked.string('Configuration/GenProduction/python/EightTeV/MSSM_mH_125_mA_2000_Hto2Ato4mu_8TeV-pythia6_cfi.py nevts:10'),
	name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
	splitLevel = cms.untracked.int32(0),
	eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
	outputCommands = process.RECOSIMEventContent.outputCommands,
	fileName = cms.untracked.string('BAM_MSSM_mH_125_mA_2000_Hto2Ato4mu_8TeV-pythia6_537p4_GEN.root'),
	dataset = cms.untracked.PSet(
	filterName = cms.untracked.string(''),
	dataTier = cms.untracked.string('GEN')
	),
	SelectEvents = cms.untracked.PSet(
		SelectEvents = cms.vstring('generation_step')
	)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:startup', '')

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
	pythiaPylistVerbosity = cms.untracked.int32(0),
	filterEfficiency = cms.untracked.double(1.0),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	comEnergy = cms.double(13000.0),
	crossSection = cms.untracked.double(1.0),
	maxEventsToPrint = cms.untracked.int32(1),
	PythiaParameters = cms.PSet(
		pythia8CommonSettingsBlock,
		pythia8CUEP8M1SettingsBlock,
		pythiaUESettings = cms.vstring(),

		processParameters = cms.vstring( #This section should be entirely in Pythia 8
			'Higgs:useBSM = on',   # initialize and use the two-Higgs-doublet BSM states
			'HiggsBSM:all = off',  # switch off all BSM Higgs processes
			'HiggsBSM:gg2H2 = on', # switch on only gg->H^0(H_2^0) process
			#'SUSY:all = on', #turn on production of SUSY particles
			'35:m0 = 125.0', #  mass of H0 in GeV
			'36:m0 = 2.0',   #  mass of A0 in GeV
			# decays of H0 (PDG ID = 35)
			'35:onMode = off',      # Turn off all decay modes 
			'35:onIfMatch = 36 36', # Allow decays to A0: H0 ->A0A0
			#decays of the A0 (PDG ID = 36)
			'36:onMode = off',       # Turn off all decay modes
			'36:onIfMatch = 13 -13', # Allow decays to muons: A0 ->mu+mu-
			'Init:showProcesses = on',        # Print a list of all processes that will be simulated, with their estimated cross section maxima
			'Init:showChangedSettings = on',  # Print a list of the changed flag/mode/parameter/word setting
			#'Init:showAllParticleData = on', # Print a list of all particle and decay data. Warning: this will be a long list
	),
		parameterSets = cms.vstring('pythiaUESettings', 
			'pythia8CommonSettings',
			'pythia8CUEP8M1Settings',
			'processParameters')
 )
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RECOSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

