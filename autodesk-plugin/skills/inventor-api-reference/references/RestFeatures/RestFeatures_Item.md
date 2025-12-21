# RestFeatures.Item Property

Parent Object: [RestFeatures](../RestFeatures/RestFeatures.md)

## Description

Returns the specified RestFeature object from the collection.

## Syntax

RestFeatures.**Item**( ***Index*** As Variant ) As [RestFeature](../RestFeature/RestFeature.md)

## Property Value

This is a read only property whose value is a [RestFeature](../RestFeature/RestFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Long or String that specifies the RestFeature object within the collection to return. Inputting a Long indicates the index of the RestFeature within the collection to return. A String can also be used to specify the name of the feature. The property will fail is the index is out of range or the name does not exist. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |