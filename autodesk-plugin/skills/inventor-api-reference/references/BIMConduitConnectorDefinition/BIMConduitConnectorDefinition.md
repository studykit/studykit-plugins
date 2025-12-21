# BIMConduitConnectorDefinition Object

Derived from: [BIMConnectorDefinition](../BIMConnectorDefinition/BIMConnectorDefinition.md) Object

## Description

BIMConduitConnectorDefinition object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ReverseDirection](../BIMConduitConnectorDefinition/BIMConduitConnectorDefinition_ReverseDirection.md) | Method that will reverse the direction of the connection. |
| [SetShape](../BIMConduitConnectorDefinition/BIMConduitConnectorDefinition_SetShape.md) | Method that used to set the shape of the connector. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BIMConduitConnectorDefinition/BIMConduitConnectorDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ConnectionType](../BIMConduitConnectorDefinition/BIMConduitConnectorDefinition_ConnectionType.md) | Read-write property that gets and sets the connection type for this connector. |
| [ConnectorShape](../BIMConduitConnectorDefinition/BIMConduitConnectorDefinition_ConnectorShape.md) | Read-only property that specifies the shape of the connector. To change the shape, use the SetShape method. |
| [Diameter](../BIMConduitConnectorDefinition/BIMConduitConnectorDefinition_Diameter.md) | Read-only property that provides access to the connector diameter. When the BIMConduitConnectorDefinition object has been created using the CreateConduitConnectorDefinition method, this property returns a Double indicating the diameter, (in centimeters), of the connector as defined by the input geometry. After the definition object has been used to create a connector, this property returns a parameter that defines the diameter of the connector.  To change the diameter of an existing connector you can either edit the geometry that’s controlling the diameter or set the override diameter using the DiameterOverride property. |
| [DiameterOverride](../BIMConduitConnectorDefinition/BIMConduitConnectorDefinition_DiameterOverride.md) | Read-write property that gets and sets the diameter override for this connector. |
| [Direction](../BIMConduitConnectorDefinition/BIMConduitConnectorDefinition_Direction.md) | Read-only property that indicates the direction of the connection. This property will return Nothing in the case where a valid set of referenced geometries have not yet been defined. |
| [Geometry](../BIMConduitConnectorDefinition/BIMConduitConnectorDefinition_Geometry.md) | Read-only property that gets the geometry that defines the shape of the connection. The returned collection is independent of the connector and any changes made to the contents of the collection will not affect the connector. To change the geometry or the shape of the connector use the SetShape method. |
| [Origin](../BIMConduitConnectorDefinition/BIMConduitConnectorDefinition_Origin.md) | Read-only property that returns the origin of the connector. |
| [Parent](../BIMConduitConnectorDefinition/BIMConduitConnectorDefinition_Parent.md) | Property that returns the parent BIMConnector that this definition is associated with. If the definition was created using one of the Create methods this property will return Nothing since the definition isn’t associated with a connector yet. |
| [Type](../BIMConduitConnectorDefinition/BIMConduitConnectorDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BIMConnectors.CreateConduitConnectorDefinition](../BIMConnectors/BIMConnectors_CreateConduitConnectorDefinition.md)

## Version

Introduced in version 2011
