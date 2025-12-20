# Parameter.Expression Property

Parent Object: [Parameter](../Parameter/Parameter.md)

## Description

Gets/(Sets) the string that denotes the algebraic expression making up the definition of this parameter. Maybe a constant. 'Set' may not be allowed on some parameter types. When set this for Text parameter, the expression value should be quoted by quotation marks at beginning and ending of a string(like """I am Jack""").

## Syntax

Parameter.**Expression**() As String

## Property Value

This is a read/write property whose value is a String.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add mate constraint with limits](../../sample-programs/AssemblyConstraints_AddMateConstraint3_Sample.md) | This sample demonstrates the creation of an assembly mate constraint with maximum and minimum limits defined. |
| [Set the value of a parameter](../../sample-programs/ParameterSetValue_Sample.md) | Sets the value of an existing parameter. A part must be open that contains a parameter named "Length". |
| [Table Parameters](../../sample-programs/ParameterTables_Sample.md) | This sample demonstrates how to access the Parameters object, and from it in turn the TableParameters collection that represents the collection of parameters that have been linked/embedded from an external spreadsheet. |
| [Sheet Metal Style Creation](../../sample-programs/SheetMetalStyles_Sample.md) | This sample illustrates creating a new sheet metal style. It uses a bend table and assumes the sample bend table delivered with Inventor is available. You can edit the path below to reference any existing bend table. To use the sample make sure a bend table is available at the specified path, open a sheet metal document, and run the sample. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |