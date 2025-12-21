# BIMCableTrayConnectorDefinition.Height Property

Parent Object: [BIMCableTrayConnectorDefinition](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition.md)

## Description

Read-only property that provides access to the connector height. When the BIMCableTrayConnectorDefinition object has been created using the CreateCableTrayConnectorDefinition method, this property returns a Double indicating the height, (in centimeters), of the connector as defined by the input geometry. After the definition object has been used to create a connector, this property returns a parameter that defines the height of the connector.

To change the height of an existing connector you can either edit the geometry that’s controlling the height or set the override height using the HeightOverride property.

## Syntax

BIMCableTrayConnectorDefinition.**Height**() As Variant

## Property Value

This is a read only property whose value is a Variant.

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |