from bs4 import BeautifulSoup
from Perk import Perk
import re

def parse_perk_page(htmlFile: str, locale = ''):
    with open(htmlFile, "r", encoding="utf8") as f:
        perks = get_perks(f.read(), "div.formattedPerkDesc")
        export_perk_names("OutputStrings/perkNames" + locale + ".xml", perks)
        export_perk_descriptions("OutputStrings/perkDescriptions" + locale + ".xml", perks)

def export_perk_names(file: str, perks: list[Perk]):
    with open(file, "w", encoding="utf8") as w:
        w.write('<?xml version="1.0" encoding="utf-8"?>\n')
        w.write("<resources>\n")
        for perk in perks:
            w.write("    <string name=\"" + perk.get_perk_name_id() + "\">" + perk.get_sanitized_name() + "</string>\n")
        w.write("</resources>\n")

def export_perk_descriptions(file: str, perks: list[Perk]):
    with open(file, "w", encoding="utf8") as w:
        w.write('<?xml version="1.0" encoding="utf-8"?>\n')
        w.write("<resources>\n")
        for perk in perks:
            w.write("    <string name=\"" + perk.get_perk_description_id() + "\">" + perk.get_sanitized_description() + "</string>\n")
        w.write("</resources>\n")

def get_perks(htmlStr: str, descType = "div.formattedPerkDesc") -> list[Perk]:
    perksHtml = BeautifulSoup(htmlStr, 'html.parser')

    perks = []
    for tableRow in perksHtml.select("tbody > tr"):
        try:
            heading = tableRow.find("th").find("a")
            perkName = heading['title']
            descriptions = tableRow.select(descType)
            imageUrl = tableRow.select("a.image")[0]['href']
            perks.append(Perk(get_slug(imageUrl), perkName, descriptions[0].text))
        except:
            print("Error getting Perk values")

    return perks

def get_slug(imageUrl: str) -> str:
    try:
        startIndex = imageUrl.find('IconPerks_') + len('IconPerks_')
        endIndex = imageUrl.find('.png')
        return re.sub('(?<!^)(?=[A-Z])', '_', imageUrl[startIndex:endIndex]).lower()
    except:
        print(f"Failed to get slug for {imageUrl}")

    return ''

"""
with open("PerkPages/Perks_fr.html", "r", encoding="utf8") as f:
    perksHtml = BeautifulSoup(f.read(), 'html.parser')
    with open("PerkPages/Tables_fr.xml", "w", encoding="utf8") as w:
        for table in perksHtml.select("table"):
            w.write(str(table))
"""

parse_perk_page("PerkPages/Perks_en.html")
parse_perk_page("PerkPages/Perks_fr.html", '_fr')
