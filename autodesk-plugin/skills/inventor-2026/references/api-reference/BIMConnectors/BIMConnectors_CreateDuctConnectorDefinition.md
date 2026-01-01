# BIMConnectors.CreateDuctConnectorDefinition Method

Parent Object: [BIMConnectors](../BIMConnectors/BIMConnectors.md)

## Description

Method that creates a new duct connector definition. The created definition object defines the inputs to create a duct connector and is used as input to the Add method of the BIMConnectors object to create a new connector.

## Syntax

BIMConnectors.**CreateDuctConnectorDefinition**( ***Geometry*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***ConnectorShape*** As [BIMConnectorShapeEnum](../BIMConnectorShapeEnum.md) ) As [BIMDuctConnectorDefinition](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Geometry | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input object collection that contains the geometry that defines the shape of the connector. When the specified shape is rectangular, valid input includes a single rectangular face or four linear edges on a planar face that define a rectangle. These edges do not need to connect but two of them need to be parallel to each other and perpendicular to the other two edge. For example, the picture below illustrates four valid lines and the resulting rectangle.  ![](../images/CableTrayDef1.png)  When the specified shape is oval, valid input includes a face that defines an oval or four edges that define an oval as illustrated below.  ![](../images/CableTrayDef2.png)  When the specified shape is circular, valid input includes a single circular face or a circular edge (it can be an arc). When the specified shape is undefined, valid input includes any of the above. |
| ConnectorShape | [BIMConnectorShapeEnum](../BIMConnectorShapeEnum.md) | Input value that specifies the shape of the connector. This setting affects how the geometry is evaluated to determine the shape of the connector. The following inputs are valid for a duct connector: kRectangularShapeConnector, kCircularShapeConnector, kOvalShapeConnector or kUndefinedShapeConnector |

## Version

Introduced in version 2011
