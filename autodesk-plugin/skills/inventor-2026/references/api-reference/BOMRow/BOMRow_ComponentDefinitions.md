# BOMRow.ComponentDefinitions Property

Parent Object: [BOMRow](../BOMRow/BOMRow.md)

## Description

Property that returns the ComponentDefinitions associated with this row in the BOM. These could be part, sheet metal, assembly, weldment or a virtual component definitions. This enumerator will return just one component definition unless this row is a merged one, in which case all associated component definitions are returned. The first component definition in the enumerator is always the primary component definition.

## Syntax

BOMRow.**ComponentDefinitions**() As [ComponentDefinitionsEnumerator](../ComponentDefinitionsEnumerator/ComponentDefinitionsEnumerator.md)

## Property Value

This is a read only property whose value is a [ComponentDefinitionsEnumerator](../ComponentDefinitionsEnumerator/ComponentDefinitionsEnumerator.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Find component referenced by balloon](../../sample-programs/BalloonValueSet_ReferencedRow_Sample.md) | This sample demonstrates how to find the component that a balloon references. |
| [Using the BOM APIs](../../sample-programs/BOM_Sample.md) | This sample demonstrates the Bill of Materials API functionality in assemblies. |

## Version

Introduced in version 10
