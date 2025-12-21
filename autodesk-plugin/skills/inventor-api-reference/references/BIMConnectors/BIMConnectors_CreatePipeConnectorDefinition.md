# BIMConnectors.CreatePipeConnectorDefinition Method

Parent Object: [BIMConnectors](../BIMConnectors/BIMConnectors.md)

## Description

Method that creates a new pipe connector definition. The created definition object defines the inputs to create a pipe connector and is used as input to the Add method of the BIMConnectors object to create a new connector.

## Syntax

BIMConnectors.**CreatePipeConnectorDefinition**( ***Geometry*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***ConnectorShape*** As [BIMConnectorShapeEnum](../BIMConnectorShapeEnum.md) ) As [BIMPipeConnectorDefinition](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Geometry | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input object collection that contains the geometry that defines the shape of the connector. When the specified shape is circular, valid input includes a single circular face or a circular edge (it can be an arc).  When the specified shape is undefined, valid input includes the input described above for a rectangular shape but also allows a rectangular planar face, four edges that define a rectangle as illustrated below:  ![](../images/CableTrayDef1.png) a planar face that has a slot shape, or four edges that define a slot or oval shape, as illustrated below. ![](../images/CableTrayDef2.png) |
| ConnectorShape | [BIMConnectorShapeEnum](../BIMConnectorShapeEnum.md) | Input value that specifies the shape of the connector. This setting affects how the geometry is evaluated to determine the shape of the connector. The following inputs are valid for a pipe connector: kCircularShapeConnector or kUndefinedShapeConnector. |

## Version

Introduced in version 2011
