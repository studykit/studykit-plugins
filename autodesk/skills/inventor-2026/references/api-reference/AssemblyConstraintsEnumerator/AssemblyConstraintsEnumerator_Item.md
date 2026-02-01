# AssemblyConstraintsEnumerator.Item Property

Parent Object: [AssemblyConstraintsEnumerator](../AssemblyConstraintsEnumerator/AssemblyConstraintsEnumerator.md)

## Description

Returns the specified AssemblyConstraint object from the collection. This is the default property of the AssemblyConstraintsEnumerator collection object.

## Syntax

AssemblyConstraintsEnumerator.**Item**( ***Index*** As Variant ) As [AssemblyConstraint](../AssemblyConstraint/AssemblyConstraint.md)

## Property Value

This is a read only property whose value is an [AssemblyConstraint](../AssemblyConstraint/AssemblyConstraint.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the constraint name. The name expected is the display name of the constraint. This is the name that is displayed to the user in the assembly browser. If an out of range index or a name of a non-existent constraint name is provided, an error occurs. |

## Version

Introduced in version 4
