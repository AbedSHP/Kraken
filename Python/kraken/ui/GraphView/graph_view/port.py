
#
# Copyright 2010-2015
#

import json
from PySide import QtGui, QtCore
from mouse_grabber import MouseGrabber


class PortLabel(QtGui.QGraphicsWidget):
    __font = QtGui.QFont('Decorative', 12)

    def __init__(self, port, text, connectionPointType, hOffset, color, highlightColor):
        super(PortLabel, self).__init__(port)
        self.__port = port
        self.__text = text
        self.__textItem = QtGui.QGraphicsTextItem(text, self)
        self._labelColor = color
        self.__highlightColor = highlightColor
        self.__textItem.setDefaultTextColor(self._labelColor)
        self.__textItem.setFont(self.__font)
        self.__textItem.translate(hOffset, -8)
        option = self.__textItem.document().defaultTextOption()
        option.setWrapMode(QtGui.QTextOption.NoWrap)
        self.__textItem.document().setDefaultTextOption(option)
        self.__textItem.adjustSize()

        self.__connectionPointType = connectionPointType

        self.setAcceptHoverEvents(True)
        self.setPreferredSize(self.textSize())
        self.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed))
        self.setWindowFrameMargins(0, 0, 0, 0)

    def text(self):
        return self.__text

    def setColor(self, color):
        self.__textItem.setDefaultTextColor(color)
        self.update()

    def textSize(self):
        return QtCore.QSizeF(
            self.__textItem.textWidth(),
            self.__font.pointSizeF()
            )

    def getPort(self):
        return self.__port

    def connectionPointType(self):
        return self.__connectionPointType

    def isInConnectionPoint(self):
        return self.__connectionPointType == 'In'

    def isOutConnectionPoint(self):
        return self.__connectionPointType == 'Out'

    # def paint(self, painter, option, widget):
    #     super(PortLabel, self).paint(painter, option, widget)
    #     painter.setPen(QtGui.QPen(QtGui.QColor(0, 0, 255)))
    #     painter.drawRect(self.windowFrameRect())

    def highlight(self):
        self.setColor(self.__highlightColor)

    def unhighlight(self):
        self.setColor(self._labelColor)

    def hoverEnterEvent(self, event):
        self.highlight()
        super(PortLabel, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.unhighlight()
        super(PortLabel, self).hoverLeaveEvent(event)

    def mousePressEvent(self, event):

        scenePos = self.mapToScene(event.pos())

        #self.unhighlight()
        if self.isInConnectionPoint():
        #     self._graph.controller().beginInteraction("Edit connection to:" + self.__port.getPath())
            MouseGrabber(self.getPort().getGraph(), scenePos, self.__port, 'Out')
        elif self.isOutConnectionPoint():
        #     self._graph.controller().beginInteraction("Edit connections from:" + self.__port.getPath())
            MouseGrabber(self.getPort().getGraph(), scenePos, self.__port, 'In')


class PortCircle(QtGui.QGraphicsWidget):
    __radius = 4.5
    __diameter = 2 * __radius

    def __init__(self, port, graph, connectionPointType, color):
        super(PortCircle, self).__init__(port)

        self.__port = port
        self._graph = graph
        self.__connectionPointType = connectionPointType

        self.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed))
        size = QtCore.QSizeF(self.__diameter, self.__diameter)
        self.setPreferredSize(size)
        self.setWindowFrameMargins(0, 0, 0, 0)

        if self.isInConnectionPoint():
            self.translate(self.__radius * -2, 0)
        else:
            self.translate(self.__radius * 2, 0)

        self.__defaultPen = QtGui.QPen(QtGui.QColor(25, 25, 25), 1.0)
        self.__hoverPen = QtGui.QPen(QtGui.QColor(255, 255, 100), 1.5)
        self.setAcceptHoverEvents(True)

        self.__ellipseItem = QtGui.QGraphicsEllipseItem()
        self.__ellipseItem.setPen(self.__defaultPen)
        self.__ellipseItem.setPos(size.width()/2, size.height()/2)
        self.__ellipseItem.setRect(
            -self.__radius,
            -self.__radius,
            self.__diameter,
            self.__diameter,
            )
        if self.isInConnectionPoint():
            self.__ellipseItem.setStartAngle(270 * 16)
            self.__ellipseItem.setSpanAngle(180 * 16)
        self.__ellipseItem.setParentItem(self)
        self.setColor(color)

    def getPort(self):
        return self.__port

    def connectionPointType(self):
        return self.__connectionPointType

    def isInConnectionPoint(self):
        return self.__connectionPointType == 'In'

    def isOutConnectionPoint(self):
        return self.__connectionPointType == 'Out'

    def centerInSceneCoords(self):
        return self.__ellipseItem.mapToScene(0, 0)

    def setColor(self, color):
        self._color = color
        self.__ellipseItem.setBrush(QtGui.QBrush(self._color))

    def highlight(self):
        self.__ellipseItem.setBrush(QtGui.QBrush(self._color.lighter()))
        # make the port bigger to highliht it can accept the connection.
        self.__ellipseItem.setRect(
            -self.__radius * 1.6,
            -self.__radius * 1.6,
            self.__diameter * 1.6,
            self.__diameter * 1.6,
            )

    def unhighlight(self):
        self.__ellipseItem.setBrush(QtGui.QBrush(self._color))
        self.__ellipseItem.setRect(
            -self.__radius,
            -self.__radius,
            self.__diameter,
            self.__diameter,
            )

    def hoverEnterEvent(self, event):
        self.highlight()
        super(PortCircle, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.unhighlight()
        super(PortCircle, self).hoverLeaveEvent(event)

    def mousePressEvent(self, event):

        scenePos = self.mapToScene(event.pos())

        self.unhighlight()

        if self.isInConnectionPoint():
            grabber = MouseGrabber(self._graph, scenePos, self.__port, 'Out')

        elif self.isOutConnectionPoint():
            grabber = MouseGrabber(self._graph, scenePos, self.__port, 'In')

    # def paint(self, painter, option, widget):
    #     super(PortCircle, self).paint(painter, option, widget)
    #     painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 0)))
    #     painter.drawRect(self.windowFrameRect())


class BasePort(QtGui.QGraphicsWidget):

    _labelColor = QtGui.QColor(25, 25, 25)
    _labelHighlightColor = QtGui.QColor(25, 25, 25).lighter(200)

    def __init__(self, parent, graph, name, color, dataType, connectionPointType):
        super(BasePort, self).__init__(parent)

        self._node = parent
        self._graph = graph
        self._name = name
        self._dataType = dataType

        self.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed))

        layout = QtGui.QGraphicsLinearLayout()
        layout.setSpacing(0)
        self.setLayout(layout)

        self._color = color

    def getName(self):
        return self._name

    def getDataType(self):
        return self._dataType

    def getNode(self):
        return self._node

    def getGraph(self):
        return self._graph

    # ===================
    # Connection Methods
    # ===================

    def getColor(self):
        return self._color

    def setColor(self, color):
        if self.__inCircle is not None:
            self.__inCircle.setColor(color)
        if self.__outCircle is not None:
            self.__outCircle.setColor(color)
        self._color = color

    # def paint(self, painter, option, widget):
    #     super(BasePort, self).paint(painter, option, widget)
    #     painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 0)))
    #     painter.drawRect(self.windowFrameRect())

    # def disconnect(self):
    #     pass
    #     self.scene().removeItem(self)


class InputPort(BasePort):
    """docstring for InputPort"""
    def __init__(self, parent, graph, name, color, dataType):
        super(InputPort, self).__init__(parent, graph, name, color, dataType, 'In')

        self.__inCircle = PortCircle(self, graph, 'In', color)
        self.layout().addItem(self.__inCircle)
        self.layout().setAlignment(self.__inCircle, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.layout().setContentsMargins(0, 0, 30, 0)
        labelHOffset = -10

        self.__labelItem = PortLabel(self, name, 'In', labelHOffset, self._labelColor, self._labelHighlightColor)
        self.layout().addItem(self.__labelItem)
        self.layout().setAlignment(self.__labelItem, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.layout().addStretch(2)

        self.__connection = None


    def inCircle(self):
        if self.__inCircle is None:
            raise Exception("Port '" + self.getNode().getName() + "." + self.__label + "' Does not have an 'In' connection point.");
        return self.__inCircle

    # ===================
    # Connection Methods
    # ===================
    def setConnection(self, connection):
        """Adds a connection to the list.
        Arguments:
        connection -- connection, new connection to add.
        Return:
        True if successful.
        """

        self.__connection = connection

        return True

    def removeConnection(self, connection):
        """Removes a connection to the list.
        Arguments:
        connection -- connection, connection to remove.
        Return:
        True if successful.
        """

        if connection != self.__connection:
            raise "Port not connected to given connection."
        self.__connection = None

        return True

    def getConnection(self):
        """Gets the ports connections list.
        Return:
        List, connections to this port.
        """

        return self.__connection


    # def disconnect(self):
        
    #     self.__connection.disconnect()




class OutputPort(BasePort):
    """docstring for OutputPort"""
    def __init__(self, parent, graph, name, color, dataType):
        super(OutputPort, self).__init__(parent, graph, name, color, dataType, 'Out')


        self.layout().addStretch(2)
        self.layout().setContentsMargins(30, 0, 0, 0)
        labelHOffset = 10

        self.__labelItem = PortLabel(self, self._name, 'Out', labelHOffset, self._labelColor, self._labelHighlightColor)
        self.layout().addItem(self.__labelItem)
        self.layout().setAlignment(self.__labelItem, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


        self.__outCircle = PortCircle(self, graph, 'Out', color)
        self.layout().addItem(self.__outCircle)
        self.layout().setAlignment(self.__outCircle, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.__connections = set()


    def outCircle(self):
        if self.__outCircle is None:
            raise Exception("Port '" + self.getNode().getName() + "." + self.__label + "' Does not have an 'Out' connection point.");
        return self.__outCircle

    # ===================
    # Connection Methods
    # ===================
    def addConnection(self, connection):
        """Adds a connection to the list.
        Arguments:
        connection -- connection, new connection to add.
        Return:
        True if successful.
        """

        self.__connections.add(connection)

        return True

    def removeConnection(self, connection):
        """Removes a connection to the list.
        Arguments:
        connection -- connection, connection to remove.
        Return:
        True if successful.
        """

        self.__connections.remove(connection)
        
        return True

    def getConnections(self):
        """Gets the ports connections list.
        Return:
        List, connections to this port.
        """

        return self.__connections

    # def disconnect(self):
    #     for connection in self.getConnections():
    #         connection.disconnect()

    # def destroy(self):

    #     for connection in self.getConnections():
    #         connection.destroy()

    #     super(OutputPort, self).destroy(self)