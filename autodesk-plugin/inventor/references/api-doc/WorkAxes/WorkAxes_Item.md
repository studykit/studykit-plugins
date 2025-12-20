# WorkAxes.Item Property

Parent Object: [WorkAxes](../WorkAxes/WorkAxes.md)

## Description

Returns the specified WorkAxis object from the collection. This is the default property of the WorkAxes collection object.

## Syntax

WorkAxes.**Item**( ***Index*** As Variant ) As [WorkAxis](../WorkAxis/WorkAxis.md)

## Property Value

This is a read only property whose value is a [WorkAxis](../WorkAxis/WorkAxis.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the object to return. This can be a numeric value indicating the index of the item in the collection or it can be a string indicating the work axis name. If an out of range index or a name of a non-existent work axis is specified, an error occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |