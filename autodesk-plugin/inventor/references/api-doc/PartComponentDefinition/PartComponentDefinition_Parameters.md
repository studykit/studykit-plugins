# PartComponentDefinition.Parameters Property

Parent Object: [PartComponentDefinition](../PartComponentDefinition/PartComponentDefinition.md)

## Description

Gets the Parameters collection object that encapsulates all of the parameters defined in this ComponentDefinition.

## Syntax

PartComponentDefinition.**Parameters**() As [Parameters](../Parameters/Parameters.md)

## Property Value

This is a read only property whose value is a [Parameters](../Parameters/Parameters.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creating a new parameter group](../../sample-programs/CustomParameterGroup_Add_Sample.md) | This sample demonstrates the creation of model, reference and user parameters and copying these parameters to a newly created group. |
| [Selectively link paramaters](../../sample-programs/DerivedParameterTables_Add2_Sample.md) | This sample demonstrates the selective linking of parameters from another Inventor file. |
| [Display information about parameter tolerances.](../../sample-programs/DumpParmeterInfo_Sample.md) | Dumps out information to the Immediate window about tolerance information associated with parameters. A part document must be active when this is run. |
| [Create user parameters](../../sample-programs/ParameterCreateUser_Sample.md) | This sample demonstrates creating user parameters using an expression and a value. A part document must be open and it must not contain user parameters named "NewParam1" and "NewParam2". |
| [Model Parameters](../../sample-programs/Parameters_Sample.md) | This sample demonstrates the methods and properties supported by the Parameters object for model parameters. |
| [Set the value of a parameter](../../sample-programs/ParameterSetValue_Sample.md) | Sets the value of an existing parameter. A part must be open that contains a parameter named "Length". |
| [Table Parameters](../../sample-programs/ParameterTables_Sample.md) | This sample demonstrates how to access the Parameters object, and from it in turn the TableParameters collection that represents the collection of parameters that have been linked/embedded from an external spreadsheet. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |