# FilletFeatureProxy.RollAlongSharpEdges Property

Parent Object: [FilletFeatureProxy](../FilletFeatureProxy/FilletFeatureProxy.md)

## Description

Property that specifies the solution method for fillets when the specified radius would cause adjacent faces to be extended. When True, the radius will be varied when necessary to preserve the edges of adjacent faces. When False, a constant radius will be maintained and adjacent faces extended as needed.

## Syntax

FilletFeatureProxy.**RollAlongSharpEdges**() As Boolean

## Property Value

This is a read only property whose value is a Boolean.

## Version

Introduced in version 9
