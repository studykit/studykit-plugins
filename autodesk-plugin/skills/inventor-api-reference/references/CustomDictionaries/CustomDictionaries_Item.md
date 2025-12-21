# CustomDictionaries.Item Property

Parent Object: [CustomDictionaries](../CustomDictionaries/CustomDictionaries.md)

## Description

Allows integer-indexed access to items in the collection.

## Syntax

CustomDictionaries.**Item**( ***Index*** As Variant ) As [CustomDictionary](../CustomDictionary/CustomDictionary.md)

## Property Value

This is a read only property whose value is a [CustomDictionary](../CustomDictionary/CustomDictionary.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the CustomDictionary to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the CustomDictionary name. If an out of range index or a name of a non-existent CustomDictionary is provided, an error will occur. |

## Version

Introduced in version 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |