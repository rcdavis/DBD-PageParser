from DBDParser import DBDParser

parser = DBDParser()
# A local HTML file can be used with the 'parse' method.
parser.parse_from_url('https://deadbydaylight.fandom.com/wiki/Perks')

parser.export_survivor_perk_names("OutputStrings/survivor_perk_name_strings.xml")
parser.export_survivor_perk_descriptions("OutputStrings/survivor_perk_descriptions_strings.xml")

parser.export_killer_perk_names("OutputStrings/killer_perk_name_strings.xml")
parser.export_killer_perk_descriptions("OutputStrings/killer_perk_descriptions_strings.xml")

parser.export_survivor_names("OutputStrings/survivor_name_strings.xml")
parser.export_killer_names("OutputStrings/killer_name_strings.xml")

parser.export_survivor_enum_class("OutputStrings/Survivor.kt")
parser.export_survivor_perk_list("OutputStrings/SurvivorPerksList.kt")

parser.export_killer_enum_class("OutputStrings/Killer.kt")
parser.export_killer_perk_list("OutputStrings/KillerPerksList.kt")

# Downloads all of the icons for perks
#parser.export_perk_icons()
