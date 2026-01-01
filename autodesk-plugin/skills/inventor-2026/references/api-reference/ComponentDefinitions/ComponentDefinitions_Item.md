# ComponentDefinitions.Item Property

Parent Object: [ComponentDefinitions](../ComponentDefinitions/ComponentDefinitions.md)

## Description

Allows integer-indexed access to objects in the collection.

## Syntax

ComponentDefinitions.**Item**( ***Index*** As Long ) As [ComponentDefinition](../ComponentDefinition/ComponentDefinition.md)

## Property Value

This is a read only property whose value is a [ComponentDefinition](../ComponentDefinition/ComponentDefinition.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Long value that specifies the index of the to return. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add mate constraint using work planes in parts](../../sample-programs/AssemblyConstraints_AddMateConstraint2_Sample.md) | This sample demonstrates creating a mate constraint between two occurrences using the work planes within those occurrences. |
| [Add mate constraint with limits](../../sample-programs/AssemblyConstraints_AddMateConstraint3_Sample.md) | This sample demonstrates the creation of an assembly mate constraint with maximum and minimum limits defined. |
| [Using the BOM APIs](../../sample-programs/BOM_Sample.md) | This sample demonstrates the Bill of Materials API functionality in assemblies. |

## Version

Introduced in version 4
