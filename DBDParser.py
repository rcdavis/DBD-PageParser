from bs4 import BeautifulSoup, Tag
from Perk import Perk

class DBDParser:
    """Parser for DBD data"""

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
        self.__survivorPerks = []
        self.__killerPerks = []
        self.parse(htmlFile)

    def get_perks(self) -> list[Perk]:
        """List of perks that were parsed.
        Returns:
            list[Perk]: List of parsed perks.
        """
        return self.__survivorPerks + self.__killerPerks

    def export_survivor_perk_names(self, xmlFile: str):
        """Exports the parsed survivor perks into a strings.xml file for perk names.
        Args:
            xmlFile (str): The strings.xml to save to for perk names.
        """
        self.__export_perk_names(xmlFile, self.__survivorPerks)

    def export_killer_perk_names(self, xmlFile: str):
        """Exports the parsed killer perks into a strings.xml file for perk names.
        Args:
            xmlFile (str): The strings.xml to save to for perk names.
        """
        self.__export_perk_names(xmlFile, self.__killerPerks)

    def __export_perk_names(self, xmlFile: str, perks: list[Perk]):
        """Exports the parsed perks into a strings.xml file for perk names.
        Args:
            xmlFile (str): The strings.xml to save to for perk names.
            perks (list[Perk]): List of perks.
        """
        with open(xmlFile, "w", encoding="utf8") as w:
            w.write(self.__stringsHeader)
            w.write("<resources>\n")
            for perk in perks:
                w.write(f'    <string name="{perk.get_perk_name_id()}">{perk.get_sanitized_name()}</string>\n')
            w.write("</resources>\n")

    def export_survivor_perk_descriptions(self, xmlFile: str):
        """Exports the parsed survivor perks into a strings.xml file for perk descriptions.
        Args:
            xmlFile (str): The strings.xml to save to for perk descriptions.
        """
        return self.__export_perk_descriptions(xmlFile, self.__survivorPerks)

    def export_killer_perk_descriptions(self, xmlFile: str):
        """Exports the parsed killer perks into a strings.xml file for perk descriptions.
        Args:
            xmlFile (str): The strings.xml to save to for perk descriptions.
        """
        return self.__export_perk_descriptions(xmlFile, self.__killerPerks)

    def __export_perk_descriptions(self, xmlFile: str, perks: list[Perk]):
        """Exports the parsed perks into a strings.xml file for perk descriptions.
        Args:
            xmlFile (str): The strings.xml to save to for perk descriptions.
            perks (list[Perk]): List of perks.
        """
        with open(xmlFile, "w", encoding="utf8") as w:
            w.write(self.__stringsHeader)
            w.write("<resources>\n")
            for perk in perks:
                w.write(f'    <string name="{perk.get_perk_description_id()}">{perk.get_sanitized_description()}</string>\n')
            w.write("</resources>\n")

    def export_survivor_names(self, xmlFile: str):
        """Exports the names of the survivors to an Android strings.
        Args:
            xmlFile (str): The Android strings file to save to.
        """
        self.__export_names(xmlFile, self.__survivorPerks, 'survivor')

    def export_killer_names(self, xmlFile: str):
        """Exports the names of the killers to an Android strings.
        Args:
            xmlFile (str): The Android strings file to save to.
        """
        self.__export_names(xmlFile, self.__killerPerks, 'killer')

    def __export_names(self, xmlFile: str, perks: list[Perk], startText: str):
        """Exports the names of the owners to an Android strings.
        Args:
            xmlFile (str): The Android strings file to save to.
            perks (list[Perk]): List of perks.
            startText (str): Label for the start of the name.
        """
        with open(xmlFile, "w", encoding="utf8") as w:
            w.write(self.__stringsHeader)
            w.write("<resources>\n")
            w.write(f'    <string name="{startText.lower()}_all">All</string>\n')
            for owner in self.__get_owners(perks):
                if owner:
                    ownerId = owner.lower().replace('é', 'e').replace('-', '_').replace('ō', 'o').replace(' ', '_')
                    w.write(f'    <string name="{startText}_{ownerId}">{owner}</string>\n')
            w.write("</resources>\n")

    def export_survivor_enum_class(self, ktFile: str):
        with open(ktFile, "w", encoding="utf8") as f:
            f.write('package dbd.dbdperks.characters\n\n')
            f.write('import androidx.annotation.DrawableRes\n')
            f.write('import androidx.annotation.StringRes\n')
            f.write('import dbd.dbdperks.R\n\n')

            f.write('enum class Survivor(\n')
            f.write('    val id: Int,\n')
            f.write('    @StringRes val nameId: Int,\n')
            f.write('    @DrawableRes val iconId: Int\n')
            f.write(') {\n')

            for index, owner in enumerate(self.__get_owners(self.__survivorPerks)):
                if owner:
                    fOwner = owner.lower().replace('é', 'e').replace('-', '_')
                    f.write(f'    {fOwner.upper()}({index}, R.string.survivor_{fOwner}, R.drawable.icon_survivor_{fOwner}),\n')
                else:
                    f.write(f'    ALL({index}, R.string.survivor_all, R.drawable.icon_survivor_all),\n')

            f.write('}\n')

    def export_survivor_perk_list(self, ktFile: str):
        with open(ktFile, "w", encoding="utf8") as f:
            f.write('package dbd.dbdperks.utils\n\n')
            f.write('import dbd.dbdperks.R\n')
            f.write('import dbd.dbdperks.characters.Survivor\n')
            f.write('import dbd.dbdperks.perks.Perk\n')
            f.write('import dbd.dbdperks.perks.PerkType\n\n')

            f.write('fun getSurvivorPerksList(): List<Perk> = listOf(\n')

            for index, perk in enumerate(self.__survivorPerks):
                owner = 'all'
                if perk.get_owner():
                    owner = perk.get_owner().upper().replace('É', 'E').replace('-', '_')

                f.write('    Perk(\n')
                f.write(f'        id = {index},\n')
                f.write(f'        nameId = R.string.{perk.get_perk_name_id()},\n')
                f.write(f'        descriptionId = R.string.{perk.get_perk_description_id()},\n')
                f.write(f'        iconId = R.drawable.icon_perk_{perk.create_string_name()},\n')
                f.write(f'        survivor = Survivor.{owner}\n')
                f.write(f'    ),\n')

            f.write(')\n')

    def parse(self, htmlFile: str):
        """Parses all data from the HTML file.
        Args:
            htmlFile (str): HTML file to parse perks from.
        """
        with open(htmlFile, 'r', encoding='utf8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

            tables = soup.find_all("table")

            self.__survivorPerks = self.__parse_perks(tables[0])
            self.__killerPerks = self.__parse_perks(tables[1])

    def __parse_perks(self, tableTag: Tag) -> list[Perk]:
        """Parses perks from the HTML Table.
        Args:
            tableTag (Tag): HTML Table that contains the perks.
        Returns:
            list[Perk]: List of parsed perks.
        """
        perks: list[Perk] = []
        for tableRow in tableTag.tbody.find_all("tr"):
            try:
                headings = tableRow.find_all("th")
                # This will be the 2nd column with the Perk name
                perkName = headings[1].a.text
                # The first <td> with be the Description column
                description = tableRow.find("td")
                # The fourth column with character info
                owner: str = None
                titleText = headings[2].find("a")
                if titleText:
                    owner = titleText.text

                perk = Perk(perkName, self.__format_perk_description_text(description), owner)
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

        htmlText = f"{tag}".replace('<div class="formattedPerkDesc">', '').replace('</div>', '')
        return htmlText.replace('<br/>', '\n').replace('\n', '\\n').replace('<td>', '').replace('</td>', '')

    def __get_owners(self, perks: list[Perk]) -> list[str]:
        owners: list[str] = []
        for perk in perks:
            if not perk.get_owner() in owners:
                owners.append(perk.get_owner())
        return owners
