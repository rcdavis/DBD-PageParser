from bs4 import BeautifulSoup, Tag
from Perk import Perk
import re

def parse_perk_page(htmlFile: str, locale = ''):
    with open(htmlFile, "r", encoding="utf8") as f:
        perks = get_perks(f.read())
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

def get_perks(htmlStr: str) -> list[Perk]:
    perksHtml = BeautifulSoup(htmlStr, 'html.parser')

    perks = []
    for tableRow in perksHtml.select("tbody > tr"):
        try:
            heading = tableRow.find("th").find("a")
            perkName = heading['title']
            descriptions = tableRow.select("div.formattedPerkDesc")
            imageUrl = tableRow.select("a.image")[0]['href']
            perk = Perk(get_slug(imageUrl), perkName, format_perk_description_text(descriptions[0]))
            if not perk in perks:
                perks.append(perk)
        except:
            print("Error getting Perk values")

    return perks

def format_perk_description_text(tag: Tag) -> str:
    tier1Color = 'color: #e8c252;'
    tier2Color = 'color: #199b1e;'
    tier3Color = 'color: #ac3ee3;'
    uniquePerkColor = 'color: #ff8800;'
    quoteColor = 'color: #e7cda2;'

    return tag.text

def get_slug(imageUrl: str) -> str:
    try:
        startIndex = imageUrl.find('IconPerks_') + len('IconPerks_')
        endIndex = imageUrl.find('.png')
        return re.sub('(?<!^)(?=[A-Z])', '_', imageUrl[startIndex:endIndex]).lower()
    except:
        print(f"Failed to get slug for {imageUrl}\n")

    return ''

"""
with open("PerkPages/Perks_fr.html", "r", encoding="utf8") as f:
    perksHtml = BeautifulSoup(f.read(), 'html.parser')
    with open("PerkPages/Tables_fr.xml", "w", encoding="utf8") as w:
        for table in perksHtml.select("table"):
            w.write(str(table))
"""

parse_perk_page("PerkPages/Perks_en.html")
#parse_perk_page("PerkPages/Perks_fr.html", '_fr')

with open('PerkPages/Perks_en.html', 'r', encoding='utf8') as f:
    tier1Color = 'color: #e8c252;'
    tier2Color = 'color: #199b1e;'
    tier3Color = 'color: #ac3ee3;'
    uniquePerkColor = 'color: #ff8800;'
    quoteColor = 'color: #e7cda2;'

    strs = []
    perksHtml = BeautifulSoup(f.read(), 'html.parser')
    for perkDesc in perksHtml.select('div.formattedPerkDesc'):
        for unwrapTag in perkDesc.select('a, i, b, p'):
            unwrapTag.unwrap()
        for imgTag in perkDesc.select('img'):
            imgTag.decompose()
        for span in perkDesc.select('span'):
            if not span.has_attr('style'):
                span.unwrap()
            elif span['style'] == tier1Color:
                span.wrap(perksHtml.new_tag('Tier1'))
                span.unwrap()
            elif span['style'] == tier2Color:
                span.wrap(perksHtml.new_tag('Tier2'))
                span.unwrap()
            elif span['style'] == tier3Color:
                span.wrap(perksHtml.new_tag('Tier3'))
                span.unwrap()
            elif span['style'] == uniquePerkColor:
                span.wrap(perksHtml.new_tag('UniquePerk'))
                span.unwrap()
            elif span['style'] == quoteColor:
                span.wrap(perksHtml.new_tag('Quote'))
                span.unwrap()
            else:
                span.unwrap()

        htmlText = f"{perkDesc}".replace('<div class="formattedPerkDesc">', '').replace('</div>', '')
        htmlText = htmlText.replace('<br/>', '\n').replace('\n', '\\n')
        strs.append(htmlText)

    with open('OutputStrings/testing.xml', 'w', encoding='utf8') as w:
        w.write('<?xml version="1.0" encoding="utf-8"?>\n')
        w.write('<resources>\n')
        for s in strs:
            w.write(f"    <string>{s}</string>\n")
        w.write('</resources>\n')

