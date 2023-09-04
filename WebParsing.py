from bs4 import BeautifulSoup, Tag
from PerkParser import PerkParser

parser = PerkParser("PerkPages/Perks_en.html")
parser.export_perk_names("OutputStrings/perkNames.xml")
parser.export_perk_descriptions("OutputStrings/perkDescriptions.xml")

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

