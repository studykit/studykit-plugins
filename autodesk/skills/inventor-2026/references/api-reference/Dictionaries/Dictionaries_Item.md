# Dictionaries.Item Property

Parent Object: [Dictionaries](../Dictionaries/Dictionaries.md)

## Description

Allows integer-indexed access to items in the collection.

## Syntax

Dictionaries.**Item**( ***Index*** As Variant ) As [Dictionary](../Dictionary/Dictionary.md)

## Property Value

This is a read only property whose value is a [Dictionary](../Dictionary/Dictionary.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the Dictionary to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the Dictionary name. If an out of range index or a name of a non-existent Dictionary is provided, an error will occur. |

## Version

Introduced in version 2020
