# DiameterModelDimensions.Item Property

Parent Object: [DiameterModelDimensions](../DiameterModelDimensions/DiameterModelDimensions.md)

## Description

Property that returns an item from the collection. You can provide either the index of the item in the collection, where the first item is index 1, or you can provide the name of the object.

## Syntax

DiameterModelDimensions.**Item**( ***Index*** As Variant ) As [DiameterModelDimension](../DiameterModelDimension/DiameterModelDimension.md)

## Property Value

This is a read only property whose value is a [DiameterModelDimension](../DiameterModelDimension/DiameterModelDimension.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the object to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the dimension name. If an out of range index or a name of a non-existent dimension is provided, an error occurs. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |