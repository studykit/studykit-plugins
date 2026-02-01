# Parameters.Item Property

Parent Object: [Parameters](../Parameters/Parameters.md)

## Description

Returns the specified Parameter object from the collection. This is the default property of the Parameters collection object.

## Syntax

Parameters.**Item**( ***Index*** As Variant ) As [Parameter](../Parameter/Parameter.md)

## Property Value

This is a read only property whose value is a [Parameter](../Parameter/Parameter.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the object to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the parameter name. If an out of range index or a name of a non-existent parameter is provided, an error occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Selectively link paramaters](../../sample-programs/DerivedParameterTables_Add2_Sample.md) | This sample demonstrates the selective linking of parameters from another Inventor file. |
| [Model Parameters](../../sample-programs/Parameters_Sample.md) | This sample demonstrates the methods and properties supported by the Parameters object for model parameters. |
| [Set the value of a parameter](../../sample-programs/ParameterSetValue_Sample.md) | Sets the value of an existing parameter. A part must be open that contains a parameter named "Length". |

## Version

Introduced in version 4
