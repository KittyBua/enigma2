from Screens.Wizard import Wizard
from Components.Label import Label
from Screens.LanguageSelection import LanguageWizard


class WizardLanguage(Wizard):
	def __init__(self, session, showSteps=True, showStepSlider=True, showList=True, showConfig=True):
		Wizard.__init__(self, session, showSteps, showStepSlider, showList, showConfig)
		self["languagetext"] = Label(_("Change Language"))
		self["backtext"] = Label(_("Previous Wizard"))
		self["nexttext"] = Label(_("Next Wizard"))

	def yellow(self):
		self.session.open(LanguageWizard)
