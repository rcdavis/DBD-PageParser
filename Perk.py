
class Perk:
    """Prepresent the name and description of a DBD Perk"""

    def __init__(self, slug: str, name: str, description: str):
        self.__slug = slug
        self.__name = name
        self.__description = description

    def get_sanitized_name(self) -> str:
        """The text that will be within the name strings.xml file with chars escaped"""
        return self.__sanitize_text(self.__name)

    def get_sanitized_description(self) -> str:
        """The text that will be within the description strings.xml file with chars escaped"""
        return self.__sanitize_text(self.__description)

    def get_perk_name_id(self) -> str:
        """The name for the string id within the name strings.xml"""
        return self.__create_string_name(self.__slug) + '_name'

    def get_perk_description_id(self) -> str:
        """The name for the string id within the description strings.xml"""
        return self.__create_string_name(self.__slug) + '_desc'

    def __sanitize_text(self, text: str) -> str:
        """Cleans up text so that it can be placed as content within strings.xml"""
        return text.replace(' ', '').replace('&', '&amp;').replace('"', '\\"').replace("'", "\\'").replace('\n', '\\n')

    def __create_string_name(self, text: str) -> str:
        """Cleans up text so that it can be defined as a name within strings.xml"""
        nameStr = 'perk_' + text.lower().replace(':', '').replace('!', '').replace("'", "")
        nameStr = nameStr.replace('-', '_').replace(' ', '_').replace('é', 'e').replace('à', 'a').replace('&', 'and')
        return nameStr

