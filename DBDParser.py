from PerkParser import PerkParser

class DBDParser:
    """Parser for Dead By Daylight data"""

    def __init__(self, htmlFile: str):
        self.__perkParser = PerkParser(htmlFile)
    
    def export_perk_names(self, xmlFile: str):
        self.__perkParser.export_perk_names(xmlFile)

    def export_perk_descriptions(self, xmlFile: str):
        self.__perkParser.export_perk_descriptions(xmlFile)
