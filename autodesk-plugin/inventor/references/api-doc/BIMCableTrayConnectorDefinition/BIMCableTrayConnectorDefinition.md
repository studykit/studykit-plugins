# BIMCableTrayConnectorDefinition Object

Derived from: [BIMConnectorDefinition](../BIMConnectorDefinition/BIMConnectorDefinition.md) Object

## Description

BIMCableTrayConnectorDefinition object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ReverseDirection](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_ReverseDirection.md) | Method that will reverse the direction of the connection. |
| [SetShape](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_SetShape.md) | Method that used to set the shape of the connector. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ConnectionType](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_ConnectionType.md) | Read-write property that gets and sets the connection type for this connector. |
| [ConnectorShape](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_ConnectorShape.md) | Read-only property that specifies the shape of the connector. To change the shape, use the SetShape method. |
| [Direction](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_Direction.md) | Read-only property that indicates the direction of the connection. This property will return Nothing in the case where a valid set of referenced geometries have not yet been defined. |
| [Geometry](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_Geometry.md) | Read-only property that gets the geometry that defines the shape of the connection. The returned collection is independent of the connector and any changes made to the contents of the collection will not affect the connector. To change the geometry or the shape of the connector use the SetShape method. |
| [Height](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_Height.md) | Read-only property that provides access to the connector height. When the BIMCableTrayConnectorDefinition object has been created using the CreateCableTrayConnectorDefinition method, this property returns a Double indicating the height, (in centimeters), of the connector as defined by the input geometry. After the definition object has been used to create a connector, this property returns a parameter that defines the height of the connector.  To change the height of an existing connector you can either edit the geometry that’s controlling the height or set the override height using the HeightOverride property. |
| [HeightDirection](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_HeightDirection.md) | Read-only property that returns the direction of the connector height. This returns Nothing in the case where the height has not yet been defined. |
| [HeightOverride](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_HeightOverride.md) | Read-write property that gets and sets the height override for this connector. |
| [Origin](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_Origin.md) | Read-only property that returns the origin of the connector. |
| [Parent](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_Parent.md) | Property that returns the parent BIMConnector that this definition is associated with. If the definition was created using one of the Create methods this property will return Nothing since the definition isn’t associated with a connector yet. |
| [Type](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Width](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_Width.md) | Read-only property that provides access to the connector width. When the BIMCableTrayConnectorDefinition object has been created using the CreateCableTrayConnectorDefinition method, this property returns a Double indicating the width, (in centimeters), of the connector as defined by the input geometry. After the definition object has been used to create a connector, this property returns a parameter that defines the width of the connector.  To change the width of an existing connector you can either edit the geometry that’s controlling the width or set the override width using the WidthOverride property. |
| [WidthDirection](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_WidthDirection.md) | Read-only property that returns the direction of the connector width. This returns Nothing in the case where the width has not yet been defined. |
| [WidthOverride](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_WidthOverride.md) | Read-write property that gets and sets the width override for this connector. |

## Accessed From

[BIMConnectors.CreateCableTrayConnectorDefinition](../BIMConnectors/BIMConnectors_CreateCableTrayConnectorDefinition.md)

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |