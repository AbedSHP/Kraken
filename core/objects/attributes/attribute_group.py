"""Kraken - objects.Attributes.attribute_group module.

Classes:
AttributeGroup - Attribute Group.

"""

class AttributeGroup(object):
    """Attribute Group that attributes belong to."""

    __kType__ = "AttributeGroup"

    def __init__(self, name):
        super(AttributeGroup, self).__init__()
        self.name = name
        self.attributes = []


    def getName(self):
        """Returns the name of the attribute.

        Return:
        String of the name of the attribute.

        """

        return self.name


    # ===============
    # Parent Methods
    # ===============
    def getParent(self):
        """Returns the paret of this attribute.

        Return:
        Parent object of this attribute.

        """

        return self.parent


    def setParent(self, parent):
        """Sets the paret of this attribute.

        Arguments:
        parent -- Object, parent object of this attribute.

        Return:
        True if successful.

        """

        self.parent = parent

        return True


    # ==============
    # kType Methods
    # ==============
    def getKType(self):
        """Returns the kType of this object.

        Return:
        True if successful.

        """

        return self.__kType__


    # ==================
    # Attribute Methods
    # ==================
    def checkAttributeIndex(self, index):
        """Checks the supplied index is valid.

        Arguments:
        index -- Integer, attribute index to check.

        Return:
        True if successful.

        """

        if index > len(self.attributes):
            raise IndexError("'" + str(index) + "' is out of the range of 'attributes' array.")

        return True


    def addAttribute(self, attribute):
        """Adds an attribute to this object.

        Arguments:
        attribute -- Object, attribute object to add to this object.

        Return:
        True if successful.

        """

        if attribute.name in [x.name for x in self.attributes]:
            raise IndexError("Child with " + attribute.name + " already exists as a attribute.")

        self.attributes.append(attribute)
        attribute.setParent(self)

        return True


    def removeAttributeByIndex(self, index):
        """Removes attribute at specified index.

        Arguments:
        index -- Integer, index of attribute to remove.

        Return:
        True if successful.

        """

        if self.checkAttributeIndex(index) is not True:
            return False

        del self.attributes[index]

        return True


    def removeAttributeByName(self, name):
        """Removes the attribute with the specified name.

        Arguments:
        name -- String, name of the attribute to remove.

        Return:
        True if successful.

        """

        removeIndex = None

        for i, eachAttribute in enumerate(self.attributes):
            if eachAttribute.name == name:
                removeIndex = i

        if removeIndex is None:
            return False

        self.removeAttributeByIndex(removeIndex)

        return True


    def getNumAttributes(self):
        """Returns the number of attributes as an integer.

        Return:
        Integer of the number of attributes on this object.

        """

        return len(self.attributes)


    def getAttributeByIndex(self, index):
        """Returns the attribute at the specified index.

        Arguments:
        index -- Integer, index of the attribute to return.

        Return:
        Attribute at the specified index.
        False if not a valid index.

        """

        if self.checkAttributeIndex(index) is not True:
            return False

        return self.attributes[index]


    def getAttributeByName(self, name):
        """Return the attribute with the specified name.

        Arguments:
        name -- String, name of the attribute to return.

        Return:
        Attribute with the specified name.
        None if not found.

        """

        for eachAttribute in self.attributes:
            if eachAttribute.name == name:
                return eachAttribute

        return None