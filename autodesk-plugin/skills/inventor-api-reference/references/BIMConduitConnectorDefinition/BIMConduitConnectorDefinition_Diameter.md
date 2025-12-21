# BIMConduitConnectorDefinition.Diameter Property

Parent Object: [BIMConduitConnectorDefinition](../BIMConduitConnectorDefinition/BIMConduitConnectorDefinition.md)

## Description

Read-only property that provides access to the connector diameter. When the BIMConduitConnectorDefinition object has been created using the CreateConduitConnectorDefinition method, this property returns a Double indicating the diameter, (in centimeters), of the connector as defined by the input geometry. After the definition object has been used to create a connector, this property returns a parameter that defines the diameter of the connector.

To change the diameter of an existing connector you can either edit the geometry that’s controlling the diameter or set the override diameter using the DiameterOverride property.

## Syntax

BIMConduitConnectorDefinition.**Diameter**() As Variant

## Property Value

This is a read only property whose value is a Variant.

## Version

Introduced in version 2011
