# FlatBendResults.Item Property

Parent Object: [FlatBendResults](../FlatBendResults/FlatBendResults.md)

## Description

Returns the specified FlatBendResultobject from the collection.

## Syntax

FlatBendResults.**Item**( ***Index*** As Variant ) As [FlatBendResult](../FlatBendResult/FlatBendResult.md)

## Property Value

This is a read only property whose value is a [FlatBendResult](../FlatBendResult/FlatBendResult.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the FlatBendResult to return. This can be a numeric value indicating the index of the item in the collection, an Edge object that belongs to the resulting bend or it can be a string indicating the InternalName of the bend. If an out of range index is provided or the InternalName of a non-existing bend is provided, an error will occur. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |