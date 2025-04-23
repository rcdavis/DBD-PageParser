
class Perk:
    """Represents the name and description of a DBD Perk.
    Attributes:
        __name (str): The name of the Perk.
        __description (str): The description of the Perk.
        __owner (str): Character that the perk comes from.
        __iconUrl (str): URL to the icon image
    """

    def __init__(self, name: str, description: str, owner: str, iconUrl: str):
        self.__name = name
        self.__description = description
        self.__owner = owner
        self.__iconUrl = iconUrl

    def get_name(self):
        return self.__name

    def get_owner(self):
        return self.__owner

    def get_icon_url(self):
        return self.__iconUrl

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
        return 'perk_' + self.create_name_slug() + '_name'

    def get_perk_description_id(self) -> str:
        """The name for the string id within the description strings.xml for Android.
        Returns:
            str: The id for the description string.
        """
        return 'perk_' + self.create_name_slug() + '_desc'

    def get_icon_name_slug(self) -> str:
        """Get the slug name of the icon for the perk.
        Returns:
            str: Slug name of the icon
        """
        return f'icon_perk_{self.create_name_slug()}'

    def __sanitize_text(self, text: str) -> str:
        """Cleans up text so that it can be placed as content within strings.xml.
        Args:
            text (str): Text to cleanup.
        Returns:
            str: The passed in text cleaned up for strings.xml content.
        """
        return text.replace(' ', '').replace('&', '&amp;').replace('"', '\\"').replace("'", "\\'").replace('\n', '\\n')

    def create_name_slug(self) -> str:
        """Cleans up name so that it can be defined as an id within strings.xml for Android.
        Returns:
            str: The name converted to an id for strings.xml (ie deja_vu).
        """
        nameStr = self.__name.lower().replace(':', '').replace('!', '').replace("'", "")
        nameStr = nameStr.replace('-', '_').replace(' ', '_').replace('__', '_').replace('&', 'and')
        nameStr = nameStr.replace('é', 'e').replace('à', 'a').replace('â', 'a')
        return nameStr

    def __eq__(self, other: object) -> bool:
        """The Equal operator"""
        if isinstance(other, Perk):
            return self.__name == other.__name and self.__description == other.__description and self.__owner == other.__owner
        return False

    def __ne__(self, other: object) -> bool:
        """The Not Equal operator"""
        return not self.__eq__(other)

    def __str__(self) -> str:
        return f"Person(name='{self.__name}', owner='{self.__owner}')"
