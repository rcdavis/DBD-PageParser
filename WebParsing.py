from bs4 import BeautifulSoup

def parseHtml(htmlStr: str):
    #perksHtml = BeautifulSoup(htmlStr, 'html.parser')

    """
    with open("strings.xml", "w", encoding="utf8") as w:
        w.write('<?xml version="1.0" encoding="utf-8"?>\n')
        w.write("<resources>\n")
        for desc in perksHtml.select("div.formattedPerkDesc"):
            perkName = desc.find_parent("td").find_parent("tr").select("th")
            print("perkName = " + perkName)
            w.write("<string name=\"" + perkName + "\">" + desc.text + "</string>\n")
        w.write("</resources>\n")
    """

    """
    with open("strings.xml", "w", encoding="utf8") as w:
        w.write('<?xml version="1.0" encoding="utf-8"?>\n')
        w.write("<resources>\n")
        for tableRow in perksHtml.select("tbody > tr"):
            heading = tableRow.find("th").find("a")
            perkName = heading['title']
            descriptions = tableRow.select("div.formattedPerkDesc")
            if descriptions.count == 0:
                continue
            w.write("<string name=\"" + createDescStringName(perkName) + "\">" + sanitizeText(descriptions[0].text) + "</string>\n")
        w.write("</resources>\n")
    """

    #writeOutDescs("rawStrings.xml", getStringDefinitions(htmlStr, "div.rawPerkDesc"))
    writeOutDescs("formattedStrings.xml", getStringDefinitions(htmlStr, "div.formattedPerkDesc"))

def writeOutDescs(file: str, descs: dict[str, str]):
    with open(file, "w", encoding="utf8") as w:
        w.write('<?xml version="1.0" encoding="utf-8"?>\n')
        w.write("<resources>\n")
        for name, text in descs.items():
            w.write("<string name=\"" + name + "\">" + text + "</string>\n")
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

            results[createDescStringName(perkName)] = sanitizeText(descriptions[0].text)
        except:
            print("Error getting string definition")

    return results

def sanitizeText(text: str) -> str:
    return text.replace(' ', '').replace('&', '&amp;').replace('"', '&quot;').replace("'", '&apos;')

def createDescStringName(text: str) -> str:
    nameStr = 'perk_' + text.lower().replace(':', '').replace('!', '').replace("'", '')
    return nameStr.replace('-', '_').replace(' ', '_').replace('é', 'e').replace('à', 'a').replace('&', 'and') + '_desc'

with open("Perks.html", "r", encoding="utf8") as f:
    parseHtml(f.read())
