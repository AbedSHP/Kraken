"""Kraken SI - SI Builder module.

Classes:
SIBuilder -- Component representation.

"""

from kraken.core.objects.curve import Curve
from kraken.core.objects.layer import Layer
from kraken.core.objects.component import BaseComponent
from kraken.core.objects.controls.base_control import BaseControl
from kraken.core.objects.attributes.bool_attribute import BoolAttribute
from kraken.core.objects.attributes.float_attribute import FloatAttribute
from kraken.core.objects.attributes.integer_attribute import IntegerAttribute
from kraken.core.objects.attributes.string_attribute import StringAttribute
from kraken.core.builders.base_builder import BaseBuilder

from utils import *


class SIBuilder(BaseBuilder):
    """Builder object for building Kraken objects in Softimage."""

    def __init__(self):
        super(SIBuilder, self).__init__()


    def buildAttributes(self, sceneItem, object3D):
        """Builds attributes on the DCC object.

        Arguments:
        sceneItem -- SceneItem, kraken object to build attributes for.
        object3D -- DCC Object, DCC object to build attributes on.

        Return:
        True if successful.

        """

        for i in xrange(sceneItem.getNumAttributes()):
            attribute = sceneItem.getAttributeByIndex(i)

            if isinstance(attribute, FloatAttribute):
                pass
                # log(attribute.name)

            elif isinstance(attribute, BoolAttribute):
                pass
                # log(attribute.name)

            elif isinstance(attribute, IntegerAttribute):
                pass
                # log(attribute.name)

            elif isinstance(attribute, StringAttribute):
                pass
                # log(attribute.name)

        return True


    def buildHierarchy(self, sceneItem, parentObject3D, component=None):
        """Builds the hierarchy for the supplied sceneItem.

        Arguments:
        sceneItem -- SceneItem, kraken object to build.
        parentObject3D -- DCC Object, object that is the parent of the created object.
        component -- Component, component that this object belongs to.

        Return:
        DCC object that was created.

        """

        if sceneItem.testFlag('guide'):
            return None

        object3D = None
        objectName = self.buildName(sceneItem, component=component)

        # Build Object
        if isinstance(sceneItem, Layer):
            object3D = parentObject3D.AddModel(None, objectName)

        elif isinstance(sceneItem, BaseComponent):
            object3D = parentObject3D.AddNull(objectName)
            component = sceneItem

        elif isinstance(sceneItem, Curve):
            object3D = parentObject3D.AddNull(objectName)

        elif isinstance(sceneItem, BaseControl):
            object3D = parentObject3D.AddNull(objectName)

        else:
            raise NotImplementedError(sceneItem.getName() + ' has an unsupported type: ' + str(type(sceneItem)))

        # Build Attributes
        if object3D is not None:
            self.buildAttributes(sceneItem, object3D)

        # Build children
        for i in xrange(sceneItem.getNumChildren()):
            child = sceneItem.getChildByIndex(i)
            self.buildHierarchy(child, object3D, component)

        return object3D


    def buildName(self, sceneItem, component=None):
        """Builds the name for the sceneItem that is passed.

        Arguments:
        sceneItem -- SceneItem, kraken object to build the name for.
        component -- Component, component that this object belongs to.

        Return:
        Built name as a string.
        None if it fails.

        """

        if isinstance(sceneItem, BaseComponent):
            return '_'.join([sceneItem.getName(), sceneItem.getSide(), 'hrc'])

        componentName = ""
        side = ""

        if component is not None:
            componentName = component.getName()
            side = component.getSide()

        if isinstance(sceneItem, Layer):
            return '_'.join([sceneItem.parent.getName(), sceneItem.getName()])

        elif isinstance(sceneItem, BaseControl):
            return '_'.join([componentName, sceneItem.getName(), side, 'ctrl'])

        elif isinstance(sceneItem, Curve):
            return '_'.join([componentName, sceneItem.getName(), side, 'crv'])

        else:
            raise NotImplementedError('buildName() not implemented for ' + str(type(sceneItem)))

        return None


    def buildTransform(self, sceneItem):
        """Translates the transform to Softimage transform.

        Arguments:
        sceneItem -- Object: object to set the transform on.

        Return:
        True if successful.

        """



        return True


    def build(self, container):
        """Builds the supplied container into a DCC representation.

        Arguments:
        container -- Container, kraken container object to build.

        Return:
        True if successful.

        """

        scnRoot = si.ActiveProject3.ActiveScene.Root

        containerNull = scnRoot.AddModel(None, container.name)

        # Create Each Component
        for eachLayer in container.getChildrenByType(Layer):
            self.buildHierarchy(eachLayer, containerNull, component=None)

        return True