from bs4 import BeautifulSoup

def parsePerkPage(htmlFile: str, locale = ''):
    with open(htmlFile, "r", encoding="utf8") as f:
        perks = getStringDefinitions(f.read(), "div.formattedPerkDesc")
        writeOutPerkNames("OutputStrings/perkNames" + locale + ".xml", perks)
        writeOutPerkDescs("OutputStrings/perkDescriptions" + locale + ".xml", perks)

def writeOutPerkNames(file: str, perks: dict[str, str]):
    with open(file, "w", encoding="utf8") as w:
        w.write('<?xml version="1.0" encoding="utf-8"?>\n')
        w.write("<resources>\n")
        for name in perks.keys():
            w.write("    <string name=\"" + createPerkStringName(name, "_name") + "\">" + sanitizeText(name) + "</string>\n")
        w.write("</resources>\n")


def writeOutPerkDescs(file: str, descs: dict[str, str]):
    with open(file, "w", encoding="utf8") as w:
        w.write('<?xml version="1.0" encoding="utf-8"?>\n')
        w.write("<resources>\n")
        for name, text in descs.items():
            w.write("    <string name=\"" + createPerkStringName(name, "_desc") + "\">" + sanitizeText(text) + "</string>\n")
        w.write("</resources>\n")


def getStringDefinitions(htmlStr: str, descType = "div.formattedPerkDesc") -> dict[str, str]:
    perksHtml = BeautifulSoup(htmlStr, 'html.parser')

    results = {}
    for tableRow in perksHtml.select("tbody > tr"):
        try:
            heading = tableRow.find("th").find("a")
            perkName = heading['title']
            descriptions = tableRow.select(descType)
            if len(descriptions) < 1:
                continue

            results[perkName] = descriptions[0].text
        except:
            print("Error getting string definition")

    return results

def sanitizeText(text: str) -> str:
    return text.replace(' ', '').replace('&', '&amp;').replace('"', '\\"').replace("'", "\\'").replace('\n', '\\n')

def createPerkStringName(text: str, endingName: str) -> str:
    nameStr = 'perk_' + text.lower().replace(':', '').replace('!', '').replace("'", "")
    nameStr = nameStr.replace('-', '_').replace(' ', '_').replace('é', 'e').replace('à', 'a').replace('&', 'and')
    return nameStr + endingName


parsePerkPage("PerkPages/Perks_en.html")
parsePerkPage("PerkPages/Perks_fr.html", '_fr')
