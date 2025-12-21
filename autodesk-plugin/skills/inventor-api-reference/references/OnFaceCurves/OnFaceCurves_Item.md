# OnFaceCurves.Item Property

Parent Object: [OnFaceCurves](../OnFaceCurves/OnFaceCurves.md)

## Description

Allows integer-indexed access to items in the collection.

## Syntax

OnFaceCurves.**Item**( ***Index*** As Long ) As [OnFaceCurve](../OnFaceCurve/OnFaceCurve.md)

## Property Value

This is a read only property whose value is an [OnFaceCurve](../OnFaceCurve/OnFaceCurve.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Variant value that specifies the OnFaceCurve to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the OnFaceCurve name. If an out of range index or a name of a non-existent OnFaceCurve is provided, an error occurs. |

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |