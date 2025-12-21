# ModelCompositeAnnotations.Item Property

Parent Object: [ModelCompositeAnnotations](../ModelCompositeAnnotations/ModelCompositeAnnotations.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

ModelCompositeAnnotations.**Item**( ***Index*** As Variant ) As [ModelCompositeAnnotation](../ModelCompositeAnnotation/ModelCompositeAnnotation.md)

## Property Value

This is a read only property whose value is a [ModelCompositeAnnotation](../ModelCompositeAnnotation/ModelCompositeAnnotation.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the index of the ModelCompositeAnnotation to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the ModelCompositeAnnotation name. If an out of range index or a name of a non-existent ModelCompositeAnnotation is provided, an error will occur. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |