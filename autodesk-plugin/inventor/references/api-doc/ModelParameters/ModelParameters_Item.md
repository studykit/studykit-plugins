# ModelParameters.Item Property

Parent Object: [ModelParameters](../ModelParameters/ModelParameters.md)

## Description

Returns the specified ModelParameter object from the collection.

## Syntax

ModelParameters.**Item**( ***Index*** As Variant ) As [ModelParameter](../ModelParameter/ModelParameter.md)

## Property Value

This is a read only property whose value is a [ModelParameter](../ModelParameter/ModelParameter.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the ModelParameter to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the parameter name. If an out of range index or a name of a non-existent parameter is provided, an error occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Model Parameters](../../sample-programs/Parameters_Sample.md) | This sample demonstrates the methods and properties supported by the Parameters object for model parameters. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |