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

    __stringsHeader = '<?xml version="1.0" encoding="utf-8"?>\n'
    __blackCircleChar = ' \u25CF '

    __renamedPerkSlugs: dict[str, str] = {
        'fixated': 'self_aware',
        'camaraderie': 'kinship',
        'surge': 'jolt',
        'cruel_limits': 'claustrophobia',
        'mindbreaker': 'fearmonger'
    }

    def __init__(self, htmlFile: str):
        self.__perks = self.__parse_perks(htmlFile)

    def get_perks(self) -> list[Perk]:
        """List of perks that were parsed.
        Returns:
            list[Perk]: List of parsed perks.
        """
        return self.__perks

    def export_perk_names(self, xmlFile: str):
        """Exports the parsed perks into a strings.xml file for perk names.
        Args:
            xmlFile (str): The strings.xml to save to for perk names.
        """
        with open(xmlFile, "w", encoding="utf8") as w:
            w.write(self.__stringsHeader)
            w.write("<resources>\n")
            for perk in self.__perks:
                w.write('    <string name="' + perk.get_perk_name_id() + '">' + perk.get_sanitized_name() + '</string>\n')
            w.write("</resources>\n")

    def export_perk_descriptions(self, xmlFile: str):
        """Exports the parsed perks into a strings.xml file for perk descriptions.
        Args:
            xmlFile (str): The strings.xml to save to for perk descriptions.
        """
        with open(xmlFile, "w", encoding="utf8") as w:
            w.write(self.__stringsHeader)
            w.write("<resources>\n")
            for perk in self.__perks:
                w.write('    <string name="' + perk.get_perk_description_id() + '">' + perk.get_sanitized_description() + '</string>\n')
            w.write("</resources>\n")

    def __parse_perks(self, htmlFile: str) -> list[Perk]:
        """Parses perks from the HTML file.
        Args:
            htmlFile (str): HTML file to parse perks from.
        Returns:
            list[Perk]: List of parsed perks.
        """
        perks: list[Perk] = []
        with open(htmlFile, 'r', encoding='utf8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

            for tableRow in soup.select("tbody > tr"):
                try:
                    headings = tableRow.find_all("th")
                    # This will be the 2nd column with the Perk name
                    perkName = headings[1].a.text
                    # The first <td> with be the Description column
                    description = tableRow.find("td")
                    perk = Perk(perkName, self.__format_perk_description_text(description))
                    if not perk in perks:
                        perks.append(perk)
                except Exception as e:
                    print(f"Error getting Perk values: {e}")

        return perks

    def __format_perk_description_text(self, tag: Tag) -> str:
        """Formats the description of perks for strings.xml.
        Args:
            tag (Tag): HTML tag that contains the perk description.
        Returns:
            str: Formatted description of the perk.
        """
        for unwrapTag in tag.select('a, i, b, p, ul, span'):
            unwrapTag.unwrap()
        for imgTag in tag.select('img'):
            imgTag.decompose()
        for listTag in tag.select('li'):
            listTag.insert_before(self.__blackCircleChar)
            listTag.unwrap()
        """for span in tag.select('span'):
            if not span.has_attr('style'):
                span.unwrap()
            elif span['style'] == self.__tier1Color:
                #newTag = soup.new_tag('font')
                #newTag['color'] = '#e8c252'
                #span.wrap(newTag)
                span.wrap(soup.new_tag('Tier1'))
                span.unwrap()
            elif span['style'] == self.__tier2Color:
                span.wrap(soup.new_tag('Tier2'))
                span.unwrap()
            elif span['style'] == self.__tier3Color:
                span.wrap(soup.new_tag('Tier3'))
                span.unwrap()
            elif span['style'] == self.__uniquePerkColor:
                span.wrap(soup.new_tag('UniquePerk'))
                span.unwrap()
            elif span['style'] == self.__quoteColor:
                span.wrap(soup.new_tag('Quote'))
                span.unwrap()
            else:
                span.unwrap()"""

        htmlText = f"{tag}".replace('<div class="formattedPerkDesc">', '').replace('</div>', '')
        return htmlText.replace('<br/>', '\n').replace('\n', '\\n').replace('<td>', '').replace('</td>', '')

