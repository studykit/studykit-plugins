# FlatPatternFeatures.Item Property

Parent Object: [FlatPatternFeatures](../FlatPatternFeatures/FlatPatternFeatures.md)

## Description

Returns the specified PartFeature object from the collection. This is limited to the features within the flat pattern.

## Syntax

FlatPatternFeatures.**Item**( ***Index*** As Variant ) As [PartFeature](../PartFeature/PartFeature.md)

## Property Value

This is a read only property whose value is a [PartFeature](../PartFeature/PartFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the PartFeature to return. This can be a numeric value indicating the index of the item in the collection or it can be a string indicating the Name of the feature. If an out of range index is provided or the name does not match an existing feature an error will occur. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |