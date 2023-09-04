from bs4 import BeautifulSoup, Tag
from Perk import Perk
import re

class PerkParser:
    """Parser for DBD Perks"""

    __tier1Color = 'color: #e8c252;'
    __tier2Color = 'color: #199b1e;'
    __tier3Color = 'color: #ac3ee3;'
    __uniquePerkColor = 'color: #ff8800;'
    __quoteColor = 'color: #e7cda2;'

    def __init__(self, htmlFile: str):
        self.__htmlFile = htmlFile
        self.__perks = self.__parse_perks()

    def get_perks(self) -> list[Perk]:
        return self.__perks

    def export_perk_names(self, xmlFile: str):
        with open(xmlFile, "w", encoding="utf8") as w:
            w.write('<?xml version="1.0" encoding="utf-8"?>\n')
            w.write("<resources>\n")
            for perk in self.__perks:
                w.write('    <string name="' + perk.get_perk_name_id() + '">' + perk.get_sanitized_name() + '</string>\n')
            w.write("</resources>\n")

    def export_perk_descriptions(self, xmlFile: str):
        with open(xmlFile, "w", encoding="utf8") as w:
            w.write('<?xml version="1.0" encoding="utf-8"?>\n')
            w.write("<resources>\n")
            for perk in self.__perks:
                w.write('    <string name="' + perk.get_perk_description_id() + '">' + perk.get_sanitized_description() + '</string>\n')
            w.write("</resources>\n")

    def __parse_perks(self) -> list[Perk]:
        with open(self.__htmlFile, 'r', encoding='utf8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

            self.__perks: list[Perk] = []
            for tableRow in soup.select("tbody > tr"):
                try:
                    heading = tableRow.find("th").find("a")
                    perkName = heading['title']
                    descriptions = tableRow.select("div.formattedPerkDesc")
                    imageUrl = tableRow.select("a.image")[0]['href']
                    perk = Perk(self.__get_slug(imageUrl), perkName, self.__format_perk_description_text(descriptions[0]))
                    if not perk in self.__perks:
                        self.__perks.append(perk)
                except:
                    print("Error getting Perk values")

        return self.__perks

    def __get_slug(self, imageUrl: str) -> str:
        try:
            startIndex = imageUrl.find('IconPerks_') + len('IconPerks_')
            endIndex = imageUrl.find('.png')
            return re.sub('(?<!^)(?=[A-Z])', '_', imageUrl[startIndex:endIndex]).lower()
        except:
            print(f"Failed to get slug for {imageUrl}\n")

        return ''

    def __format_perk_description_text(self, tag: Tag) -> str:
        return tag.text

    def get_formatted_description(self):
        strs = []

        with open(self.__htmlFile, 'r', encoding='utf8') as f:
            perksHtml = BeautifulSoup(f.read(), 'html.parser')
            for perkDesc in perksHtml.select('div.formattedPerkDesc'):
                for unwrapTag in perkDesc.select('a, i, b, p, ul'):
                    unwrapTag.unwrap()
                for imgTag in perkDesc.select('img'):
                    imgTag.decompose()
                for listTag in perkDesc.select("li"):
                    listTag.insert_before(' \u25CF ')
                    listTag.unwrap()
                for span in perkDesc.select('span'):
                    if not span.has_attr('style'):
                        span.unwrap()
                    elif span['style'] == self.__tier1Color:
                        span.wrap(perksHtml.new_tag('Tier1'))
                        span.unwrap()
                    elif span['style'] == self.__tier2Color:
                        span.wrap(perksHtml.new_tag('Tier2'))
                        span.unwrap()
                    elif span['style'] == self.__tier3Color:
                        span.wrap(perksHtml.new_tag('Tier3'))
                        span.unwrap()
                    elif span['style'] == self.__uniquePerkColor:
                        span.wrap(perksHtml.new_tag('UniquePerk'))
                        span.unwrap()
                    elif span['style'] == self.__quoteColor:
                        span.wrap(perksHtml.new_tag('Quote'))
                        span.unwrap()
                    else:
                        span.unwrap()

                htmlText = f"{perkDesc}".replace('<div class="formattedPerkDesc">', '').replace('</div>', '')
                htmlText = htmlText.replace('<br/>', '\n').replace('\n', '\\n')
                strs.append(htmlText)

        with open(f"OutputStrings/Perks-testing.xml", 'w', encoding='utf8') as w:
            w.write('<?xml version="1.0" encoding="utf-8"?>\n')
            w.write('<resources>\n')
            for s in strs:
                w.write(f"    <string>{s}</string>\n")
            w.write('</resources>\n')
