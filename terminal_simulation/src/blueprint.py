import xml.etree.ElementTree as ET

class Blueprint:
    """
    The Blueprint class is responsible for parsing XML blueprint files.
    """

    def __init__(self, path):
        """
        Initializes a new Blueprint object.

        Args:
            path (str): The path to the XML blueprint file.
        """
        self.path = path
        self.tree = ET.parse(path)
        self.root = self.tree.getroot()

    def get_type(self):
        """
        Returns the type of the blueprint.

        Returns:
            str: The type of the blueprint.
        """
        return self.root.find("type").text

    def get_name(self):
        """
        Returns the name of the blueprint.

        Returns:
            str: The name of the blueprint.
        """
        return self.root.find("name").text

    def get_species(self):
        """
        Returns the species of the blueprint.

        Returns:
            str: The species of the blueprint.
        """
        return self.root.find("species").text

    def get_attributes(self):
        """
        Returns the attributes of the blueprint.

        Returns:
            dict: A dictionary of the blueprint's attributes.
        """
        attributes = {}
        for attribute in self.root.find("attributes"):
            attributes[attribute.tag] = int(attribute.text)
        return attributes
