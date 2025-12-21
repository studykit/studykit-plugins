# BIMConnectorDefinition Object

## Description

BIMConnectorDefinition object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ReverseDirection](../BIMConnectorDefinition/BIMConnectorDefinition_ReverseDirection.md) | Method that will reverse the direction of the connection. |
| [SetShape](../BIMConnectorDefinition/BIMConnectorDefinition_SetShape.md) | Method that used to set the shape of the connector. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BIMConnectorDefinition/BIMConnectorDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ConnectorShape](../BIMConnectorDefinition/BIMConnectorDefinition_ConnectorShape.md) | Read-only property that specifies the shape of the connector. To change the shape, use the SetShape method. |
| [Direction](../BIMConnectorDefinition/BIMConnectorDefinition_Direction.md) | Read-only property that indicates the direction of the connection. This property will return Nothing in the case where a valid set of referenced geometries have not yet been defined. |
| [Geometry](../BIMConnectorDefinition/BIMConnectorDefinition_Geometry.md) | Read-only property that gets the geometry that defines the shape of the connection. The returned collection is independent of the connector and any changes made to the contents of the collection will not affect the connector. To change the geometry or the shape of the connector use the SetShape method. |
| [Origin](../BIMConnectorDefinition/BIMConnectorDefinition_Origin.md) | Read-only property that returns the origin of the connector. |
| [Parent](../BIMConnectorDefinition/BIMConnectorDefinition_Parent.md) | Property that returns the parent BIMConnector that this definition is associated with. If the definition was created using one of the Create methods this property will return Nothing since the definition isn’t associated with a connector yet. |
| [Type](../BIMConnectorDefinition/BIMConnectorDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BIMConnector.Definition](../BIMConnector/BIMConnector_Definition.md)

## Derived Classes

[BIMCableTrayConnectorDefinition](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition.md), [BIMConduitConnectorDefinition](../BIMConduitConnectorDefinition/BIMConduitConnectorDefinition.md), [BIMDuctConnectorDefinition](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition.md), [BIMElectricalConnectorDefinition](../BIMElectricalConnectorDefinition/BIMElectricalConnectorDefinition.md), [BIMPipeConnectorDefinition](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition.md)

## Version

Introduced in version 2011
