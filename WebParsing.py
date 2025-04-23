from DBDParser import DBDParser

"""parser = PerkParser("PerkPages/Perks_en.html")
parser.export_perk_names("OutputStrings/perkNames.xml")
parser.export_perk_descriptions("OutputStrings/perkDescriptions.xml")"""

parser = DBDParser("PerkPages/PerksNew.html")
parser.export_perk_names("OutputStrings/perkNamesNew.xml")
parser.export_perk_descriptions("OutputStrings/perkDescriptionsNew.xml")

"""parser = PerkParser("PerkPages/Perks_fr.html")
parser.export_perk_names("OutputStrings/perkNames_fr.xml")
parser.export_perk_descriptions("OutputStrings/perkDescriptions_fr.xml")

parser = PerkParser("PerkPages/Perks_New.html")
parser.export_perk_names("OutputStrings/perkNames_norm.xml")
parser.export_perk_descriptions("OutpuStrings/perkDescriptions_norm.xml")"""
