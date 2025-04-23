
class Perk:
    """Represents the name and description of a DBD Perk.
    Attributes:
        __name (str): The name of the Perk.
        __description (str): The description of the Perk.
    """

    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    def get_sanitized_name(self) -> str:
        """The text that will be within the name strings.xml file with chars escaped.
        Returns:
            str: Text within the name string.
        """
        return self.__sanitize_text(self.__name)

    def get_sanitized_description(self) -> str:
        """The text that will be within the description strings.xml file with chars escaped.
        Returns:
            str: Text within the description string.
        """
        return self.__sanitize_text(self.__description)

    def get_perk_name_id(self) -> str:
        """The name for the string id within the name strings.xml for Android.
        Returns:
            str: The id for the name string.
        """
        return self.__create_string_name(self.__name) + '_name'

    def get_perk_description_id(self) -> str:
        """The name for the string id within the description strings.xml for Android.
        Returns:
            str: The id for the description string.
        """
        return self.__create_string_name(self.__name) + '_desc'

    def __sanitize_text(self, text: str) -> str:
        """Cleans up text so that it can be placed as content within strings.xml.
        Args:
            text (str): Text to cleanup.
        Returns:
            str: The passed in text cleaned up for strings.xml content.
        """
        return text.replace(' ', '').replace('&', '&amp;').replace('"', '\\"').replace("'", "\\'").replace('\n', '\\n')

    def __create_string_name(self, name: str) -> str:
        """Cleans up name so that it can be defined as an id within strings.xml for Android.
        Args:
            name (str): The name to clean up.
        Returns:
            str: The name converted to an id for strings.xml (ie perk_deja_vu).
        """
        nameStr = 'perk_' + name.lower().replace(':', '').replace('!', '').replace("'", "")
        nameStr = nameStr.replace('-', '_').replace(' ', '_').replace('__', '_').replace('&', 'and')
        nameStr = nameStr.replace('é', 'e').replace('à', 'a').replace('â', 'a')
        return nameStr

    def __eq__(self, other: object) -> bool:
        """The Equal operator"""
        if isinstance(other, Perk):
            return self.__name == other.__name and self.__description == other.__description
        return False

    def __ne__(self, other: object) -> bool:
        """The Not Equal operator"""
        return not self.__eq__(other)

