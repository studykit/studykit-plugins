# BIMDuctConnectorDefinition.SetShape Method

Parent Object: [BIMDuctConnectorDefinition](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition.md)

## Description

Method that used to set the shape of the connector.

## Syntax

BIMDuctConnectorDefinition.**SetShape**( ***Geometry*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***ConnectorShape***] As [BIMConnectorShapeEnum](../BIMConnectorShapeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Geometry | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that specifies the set of geometry used to define the connector position and shape. |
| ConnectorShape | [BIMConnectorShapeEnum](../BIMConnectorShapeEnum.md) | Input value that indicates the desired shape of the connector and how the geometry is to be evaluated. Valid values for the various types of connectors is shown below.   * Cable tray connectors: kRectangularShapeConnector or kUndefinedShapeConnector * Conduit connectors: kCircularShapeConnector or kUndefinedShapeConnector * Duct connectors: kRectangularShapeConnector, kCircularShapeConnector, kOvalShapeConnector or kUndefinedShapeConnector * Electrical connectors: kUndefinedShapeConnector * Pipe connectors: kCircularShapeConnector or kUndefinedShapeConnector   The input geometry for the various shapes can be the following:   * Circular shape   + Single circular face.   + Circular edge (it can be an arc) * Rectangular shape   + Rectangular planar face.   + Four edges that define a rectangle as illustrated below. ![](../images/CableTrayDef1.png) * Slot shape   + Planar face that has a slot shape.   + Four edges that define a slot or oval shape, as illustrated below ![](../images/CableTrayDef2.png) |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |