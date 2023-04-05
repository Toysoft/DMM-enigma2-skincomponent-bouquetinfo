from Components.Converter.Converter import Converter
from enigma import iPlayableService, eServiceCenter
from Components.Element import cached

class BouquetInfo(Converter, object):
	BOUQUETNAME = 0

	def __init__(self, type):
		Converter.__init__(self, type)

		self.type, self.interesting_events = {
				"BouquetName": (self.BOUQUETNAME, (iPlayableService.evStart,)),
			}[type]

	@cached
	def getText(self):
		if self.type == self.BOUQUETNAME:
			from Screens.InfoBar import InfoBar
			bouquet = InfoBar.instance.servicelist.getRoot()
			if bouquet and bouquet.valid():
				info = eServiceCenter.getInstance().info(bouquet)
				bouquetname = info and info.getName(bouquet) or ""
			return bouquetname
		return ""

	text = property(getText)

	def changed(self, what):
		if what[0] != self.CHANGED_SPECIFIC or what[1] in self.interesting_events:
			Converter.changed(self, what)
