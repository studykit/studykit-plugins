# BIMPipeConnectorDefinition.Diameter Property

Parent Object: [BIMPipeConnectorDefinition](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition.md)

## Description

Read-only property that provides access to the connector diameter. When the BIMPipeConnectorDefinition object has been created using the CreateBIMPipeConnectorDefinition method, this property returns a Double indicating the diameter, (in centimeters), of the connector as defined by the input geometry. After the definition object has been used to create a connector, this property returns a parameter that defines the diameter of the connector.

To change the diameter of an existing connector you can either edit the geometry that’s controlling the diameter or set the override diameter using the DiameterOverride property.

## Syntax

BIMPipeConnectorDefinition.**Diameter**() As Variant

## Property Value

This is a read only property whose value is a Variant.

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |