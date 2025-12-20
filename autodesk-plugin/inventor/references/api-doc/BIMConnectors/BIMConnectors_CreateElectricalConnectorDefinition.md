# BIMConnectors.CreateElectricalConnectorDefinition Method

Parent Object: [BIMConnectors](../BIMConnectors/BIMConnectors.md)

## Description

Method that creates a new electrical connector definition. The created definition object defines the inputs to create a electrical connector and is used as input to the Add method of the BIMConnectors object to create a new connector.

## Syntax

BIMConnectors.**CreateElectricalConnectorDefinition**( ***Geometry*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md) ) As [BIMElectricalConnectorDefinition](../BIMElectricalConnectorDefinition/BIMElectricalConnectorDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Geometry | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input object collection that contains the geometry that defines the shape of the connector. Valid input includes:  * Single circular face. * Circular edge (it can be an arc) * Rectangular planar face. * Four edges that define a rectangle as illustrated below. ![](../images/CableTrayDef1.png) * Planar face that has a slot shape. * Four edges that define a slot or oval shape, as illustrated below.  ![](../images/CableTrayDef2.png) |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |