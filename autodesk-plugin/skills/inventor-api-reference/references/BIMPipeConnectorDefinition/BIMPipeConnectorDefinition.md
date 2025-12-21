# BIMPipeConnectorDefinition Object

Derived from: [BIMConnectorDefinition](../BIMConnectorDefinition/BIMConnectorDefinition.md) Object

## Description

BIMPipeConnectorDefinition object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ReverseDirection](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_ReverseDirection.md) | Method that will reverse the direction of the connection. |
| [SetShape](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_SetShape.md) | Method that used to set the shape of the connector. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllowSlopeAdjustment](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_AllowSlopeAdjustment.md) | Read-write property that gets and sets whether or not slope adjustment is allowed for this connector. |
| [AllowSlopeAdjustmentParameter](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_AllowSlopeAdjustmentParameter.md) | Read-write property that gets and sets the AllowSlopeAdjustment with expression or parameter. |
| [Application](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ConnectionType](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_ConnectionType.md) | Read-write property that gets and sets the connection type for this connector. |
| [ConnectorShape](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_ConnectorShape.md) | Read-only property that specifies the shape of the connector. To change the shape, use the SetShape method. |
| [Description](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_Description.md) | Read-write property that gets and sets the description of this connector. |
| [DescriptionParameter](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_DescriptionParameter.md) | Read-write property that gets and sets the description with expression or parameter. |
| [Diameter](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_Diameter.md) | Read-only property that provides access to the connector diameter. When the BIMPipeConnectorDefinition object has been created using the CreateBIMPipeConnectorDefinition method, this property returns a Double indicating the diameter, (in centimeters), of the connector as defined by the input geometry. After the definition object has been used to create a connector, this property returns a parameter that defines the diameter of the connector.  To change the diameter of an existing connector you can either edit the geometry that’s controlling the diameter or set the override diameter using the DiameterOverride property. |
| [DiameterOverride](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_DiameterOverride.md) | Read-write property that gets and sets the diameter override for this connector. |
| [Direction](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_Direction.md) | Read-only property that indicates the direction of the connection. This property will return Nothing in the case where a valid set of referenced geometries have not yet been defined. |
| [ExposeAllowSlopeAdjustmentAsParameter](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_ExposeAllowSlopeAdjustmentAsParameter.md) | Read-write property that gets and sets if expose the AllowSlopeAdjustment as parameter. |
| [ExposeDescriptionAsParameter](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_ExposeDescriptionAsParameter.md) | Read-write property that gets and sets if expose the description as parameter. |
| [ExposeFlowValueAsParameter](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_ExposeFlowValueAsParameter.md) | Read-write property that gets and sets if expose the flow value as parameter. |
| [ExposeLossValueAsParameter](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_ExposeLossValueAsParameter.md) | Read-write property that gets and sets if expose the loss value as parameter. |
| [FlowConfiguration](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_FlowConfiguration.md) | Read-write property that gets and sets the flow configuration used for this connector. |
| [FlowDirection](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_FlowDirection.md) | Read-write property that gets and sets the flow direction for this pipe connector. |
| [FlowValue](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_FlowValue.md) | Read-write property that gets and sets the value for the flow. |
| [FlowValueParameter](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_FlowValueParameter.md) | Read-write property that gets and sets the flow value with expression or parameter. |
| [Geometry](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_Geometry.md) | Read-only property that gets the geometry that defines the shape of the connection. The returned collection is independent of the connector and any changes made to the contents of the collection will not affect the connector. To change the geometry or the shape of the connector use the SetShape method. |
| [LossMethod](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_LossMethod.md) | Read-write property that gets and sets the loss method used for this connector. |
| [LossValue](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_LossValue.md) | Read-write property that gets and sets the value for the loss method. |
| [LossValueParameter](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_LossValueParameter.md) | Read-write property that gets and sets the loss value with expression or parameter. |
| [NominalDiameter](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_NominalDiameter.md) | Read-write property that provides access to the nominal diameter of the pipe connection. |
| [Origin](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_Origin.md) | Read-only property that returns the origin of the connector. |
| [Parent](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_Parent.md) | Property that returns the parent BIMConnector that this definition is associated with. If the definition was created using one of the Create methods this property will return Nothing since the definition isn’t associated with a connector yet. |
| [SystemType](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_SystemType.md) | Read-write property that specifies the system type for this connector. |
| [Type](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BIMConnectors.CreatePipeConnectorDefinition](../BIMConnectors/BIMConnectors_CreatePipeConnectorDefinition.md)

## Version

Introduced in version 2011
