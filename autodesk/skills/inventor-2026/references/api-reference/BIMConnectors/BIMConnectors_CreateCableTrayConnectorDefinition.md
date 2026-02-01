# BIMConnectors.CreateCableTrayConnectorDefinition Method

Parent Object: [BIMConnectors](../BIMConnectors/BIMConnectors.md)

## Description

Method that creates a new cable tray connector definition. The created definition object defines the inputs to create a cable tray connector and is used as input to the Add method of the BIMConnectors object to create a new connector.

## Remarks

The created definition defaults to a rectangular shape, the height and width are defined by the input geometry, and the connection type is electrically bonded. You can change any of these settings by using the methods and properties on the returned BIMCableTrayConnectorDefinition.

## Syntax

BIMConnectors.**CreateCableTrayConnectorDefinition**( ***Geometry*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***ConnectorShape*** As [BIMConnectorShapeEnum](../BIMConnectorShapeEnum.md) ) As [BIMCableTrayConnectorDefinition](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Geometry | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input object collection that contains the geometry that defines the shape of the connector. When the specified shape is rectangular, valid input includes a single rectangular face or four linear edges on a planar face that define a rectangle. These edges do not need to connect but two of them need to be parallel to each other and perpendicular to the other two edge. For example, the picture below illustrates four valid lines and the resulting rectangle.  ![](../images/CableTrayDef1.png)  When the specified shape is undefined, valid input includes the input described above for a rectangular shape but also allows a circular planar face, a circular edge (it can be an arc), a planar face that has a slot shape, or four edges that define a slot or oval shape, as illustrated below.  ![](../images/CableTrayDef2.png) |
| ConnectorShape | [BIMConnectorShapeEnum](../BIMConnectorShapeEnum.md) | Input value that specifies the shape of the connector. This setting affects how the geometry is evaluated to determine the shape of the connector. The following inputs are valid for a cable tray connector: kRectangularShapeConnector or kUndefinedShapeConnector |

## Version

Introduced in version 2011
