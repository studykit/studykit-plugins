# Sheets.Item Property

Parent Object: [Sheets](../Sheets/Sheets.md)

## Description

Returns the specified Sheet object from the collection.

## Syntax

Sheets.**Item**( ***Index*** As Variant ) As [Sheet](../Sheet/Sheet.md)

## Property Value

This is a read only property whose value is a [Sheet](../Sheet/Sheet.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the Sheet to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the sheet's name. If an out-of-range index or a name of a non-existent Sheet is specified, an error occurs. |

## Version

Introduced in version 4
