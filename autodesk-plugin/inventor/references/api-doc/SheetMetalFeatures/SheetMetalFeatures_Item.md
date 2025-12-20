# SheetMetalFeatures.Item Property

Parent Object: [SheetMetalFeatures](../SheetMetalFeatures/SheetMetalFeatures.md)

## Description

Returns the specified PartFeature object from the collection. It accesses all of the features regardless of their type. If you increment through the features in the collection they are returned in the same order as they appear in the feature browser.

## Syntax

SheetMetalFeatures.**Item**( ***Index*** As Variant ) As [PartFeature](../PartFeature/PartFeature.md)

## Property Value

This is a read only property whose value is a [PartFeature](../PartFeature/PartFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the feature to return. This can be either a numeric value indicating the index of the item in the collection or it can be a String indicating the feature name. If an out of range index or a name of a non-existent feature is provided, an error occurs. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |