# BIMPipeConnectorDefinition.Geometry Property

Parent Object: [BIMPipeConnectorDefinition](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition.md)

## Description

Read-only property that gets the geometry that defines the shape of the connection. The returned collection is independent of the connector and any changes made to the contents of the collection will not affect the connector. To change the geometry or the shape of the connector use the SetShape method.

## Syntax

BIMPipeConnectorDefinition.**Geometry**() As [ObjectCollection](../ObjectCollection/ObjectCollection.md)

## Property Value

This is a read only property whose value is an [ObjectCollection](../ObjectCollection/ObjectCollection.md).

## Version

Introduced in version 2011
