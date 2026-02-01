# BIMDuctConnectorDefinition Object

Derived from: [BIMConnectorDefinition](../BIMConnectorDefinition/BIMConnectorDefinition.md) Object

## Description

BIMDuctConnectorDefinition object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ReverseDirection](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_ReverseDirection.md) | Method that will reverse the direction of the connection. |
| [SetShape](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_SetShape.md) | Method that used to set the shape of the connector. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ConnectionType](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_ConnectionType.md) | Read-write property that gets and sets the connection type for this connector. |
| [ConnectorShape](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_ConnectorShape.md) | Read-only property that specifies the shape of the connector. To change the shape, use the SetShape method. |
| [Description](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_Description.md) | Read-write property that gets and sets the description of this connector. |
| [DescriptionParameter](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_DescriptionParameter.md) | Read-write property that gets and sets the description with expression or parameter. |
| [Diameter](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_Diameter.md) | Read-only property that provides access to the connector diameter. When the BIMDuctConnectorDefinition object has been created using the CreateBIMDuctConnectorDefinition method, this property returns a Double indicating the diameter, (in centimeters), of the connector as defined by the input geometry. After the definition object has been used to create a connector, this property returns a parameter that defines the diameter of the connector.  To change the diameter of an existing connector you can either edit the geometry that’s controlling the diameter or set the override diameter using the DiameterOverride property. |
| [DiameterOverride](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_DiameterOverride.md) | Read-write property that gets and sets the diameter override for this connector. |
| [Direction](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_Direction.md) | Read-only property that indicates the direction of the connection. This property will return Nothing in the case where a valid set of referenced geometries have not yet been defined. |
| [ExposeDescriptionAsParameter](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_ExposeDescriptionAsParameter.md) | Read-write property that gets and sets if expose the description as parameter. |
| [ExposeFlowValueAsParameter](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_ExposeFlowValueAsParameter.md) | Read-write property that gets and sets if expose the flow value as parameter. |
| [ExposeLossValueAsParameter](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_ExposeLossValueAsParameter.md) | Read-write property that gets and sets if expose the loss value as parameter. |
| [FlowConfiguration](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_FlowConfiguration.md) | Read-write property that gets and sets the flow configuration used for this connector. |
| [FlowDirection](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_FlowDirection.md) | Read-write property that gets and sets the flow direction for this Duct connector. |
| [FlowValue](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_FlowValue.md) | Read-write property that gets and sets the value for the flow. |
| [FlowValueParameter](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_FlowValueParameter.md) | Read-write property that gets and sets the flow value with expression or parameter. |
| [Geometry](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_Geometry.md) | Read-only property that gets the geometry that defines the shape of the connection. The returned collection is independent of the connector and any changes made to the contents of the collection will not affect the connector. To change the geometry or the shape of the connector use the SetShape method. |
| [Height](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_Height.md) | Read-only property that provides access to the connector height. When the BIMDuctConnectorDefinition object has been created using the CreateBIMDuctConnectorDefinition method, this property returns a Double indicating the height, (in centimeters), of the connector as defined by the input geometry. After the definition object has been used to create a connector, this property returns a parameter that defines the height of the connector.  To change the height of an existing connector you can either edit the geometry that’s controlling the height or set the override height using the HeightOverride property. |
| [HeightDirection](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_HeightDirection.md) | Read-only property that returns the direction of the connector height. This returns Nothing in the case where the height has not yet been defined. |
| [HeightOverride](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_HeightOverride.md) | Read-write property that gets and sets the height override for this connector. |
| [LossMethod](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_LossMethod.md) | Read-write property that gets and sets the loss method used for this connector. |
| [LossValue](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_LossValue.md) | Read-write property that gets and sets the value for the loss method. |
| [LossValueParameter](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_LossValueParameter.md) | Read-write property that gets and sets the loss value with expression or parameter. |
| [Origin](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_Origin.md) | Read-only property that returns the origin of the connector. |
| [Parent](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_Parent.md) | Property that returns the parent BIMConnector that this definition is associated with. If the definition was created using one of the Create methods this property will return Nothing since the definition isn’t associated with a connector yet. |
| [SystemType](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_SystemType.md) | Read-write property that specifies the system type for this connector. |
| [Type](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Width](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_Width.md) | Read-only property that provides access to the connector width. When the BIMDuctConnectorDefinition object has been created using the CreateBIMDuctConnectorDefinition method, this property returns a Double indicating the width, (in centimeters), of the connector as defined by the input geometry. After the definition object has been used to create a connector, this property returns a parameter that defines the width of the connector.  To change the width of an existing connector you can either edit the geometry that’s controlling the width or set the override width using the WidthOverride property. |
| [WidthDirection](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_WidthDirection.md) | Read-only property that returns the direction of the connector width. This returns Nothing in the case where the width has not yet been defined. |
| [WidthOverride](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_WidthOverride.md) | Read-write property that gets and sets the width override for this connector. |

## Accessed From

[BIMConnectors.CreateDuctConnectorDefinition](../BIMConnectors/BIMConnectors_CreateDuctConnectorDefinition.md)

## Version

Introduced in version 2011
