# RipFeatures.Item Property

Parent Object: [RipFeatures](../RipFeatures/RipFeatures.md)

## Description

Returns the specified RipFeature object from the collection.

## Syntax

RipFeatures.**Item**( ***Index*** As Variant ) As [RipFeature](../RipFeature/RipFeature.md)

## Property Value

This is a read only property whose value is a [RipFeature](../RipFeature/RipFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Long or String that specifies the RipFeature object within the collection to return. Inputting a Long indicates the index of the RipFeature within the collection to return. A String can also be used to specify the name of the feature. The property will fail is the index is out of range or the name does not exist. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |