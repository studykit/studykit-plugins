# FilletSetback.Edge Property

Parent Object: [FilletSetback](../FilletSetback/FilletSetback.md)

## Description

Property that returns the associated with this setback. This property is only available when a FilletDefinition object is being defined to use as input for creating a fillet. When the parent FilletDefinition object is obtained from an existing Fillet, the end-of-part marker should be placed above this fillet feature to allow access this property.

## Syntax

FilletSetback.**Edge**() As [Edge](../Edge/Edge.md)

## Property Value

This is a read only property whose value is an [Edge](../Edge/Edge.md).

## Version

Introduced in version 5.3
