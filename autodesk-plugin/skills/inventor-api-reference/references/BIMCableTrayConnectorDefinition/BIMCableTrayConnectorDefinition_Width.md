# BIMCableTrayConnectorDefinition.Width Property

Parent Object: [BIMCableTrayConnectorDefinition](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition.md)

## Description

Read-only property that provides access to the connector width. When the BIMCableTrayConnectorDefinition object has been created using the CreateCableTrayConnectorDefinition method, this property returns a Double indicating the width, (in centimeters), of the connector as defined by the input geometry. After the definition object has been used to create a connector, this property returns a parameter that defines the width of the connector.

To change the width of an existing connector you can either edit the geometry that’s controlling the width or set the override width using the WidthOverride property.

## Syntax

BIMCableTrayConnectorDefinition.**Width**() As Variant

## Property Value

This is a read only property whose value is a Variant.

## Version

Introduced in version 2011
