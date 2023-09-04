from PerkParser import PerkParser

parser = PerkParser("PerkPages/Perks_en.html")
parser.export_perk_names("OutputStrings/perkNames.xml")
parser.export_perk_descriptions("OutputStrings/perkDescriptions.xml")

parser.get_formatted_description()
