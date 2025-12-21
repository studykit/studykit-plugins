# SketchBlockDefinitions.Item Property

Parent Object: [SketchBlockDefinitions](../SketchBlockDefinitions/SketchBlockDefinitions.md)

## Description

Returns the specified SketchBlockDefinition object from the collection.

## Syntax

SketchBlockDefinitions.**Item**( ***Index*** As Variant ) As [SketchBlockDefinition](../SketchBlockDefinition/SketchBlockDefinition.md)

## Property Value

This is a read only property whose value is a [SketchBlockDefinition](../SketchBlockDefinition/SketchBlockDefinition.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the SketchBlockDefinition to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the SketchBlockDefinition name. If an out of range index or a name of a non\-existent SketchBlockDefinition is provided, an error will occur. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create and insert a sketch block definition into a part sketch](../../sample-programs/SketchBlockDefinition_Sample.md) | This sample demonstrates inserting a sketch block into a part sketch. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |