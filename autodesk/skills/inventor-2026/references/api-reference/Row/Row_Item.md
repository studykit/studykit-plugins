# Row.Item Property

Parent Object: [Row](../Row/Row.md)

## Description

Returns the specified Cell object from the collection.

## Syntax

Row.**Item**( ***Index*** As Variant ) As [Cell](../Cell/Cell.md)

## Property Value

This is a read only property whose value is a [Cell](../Cell/Cell.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the Cell to return. This can be either a numeric value indicating the index of the item in the collection, a string indicating the title of a column header, or a Column object. If an out of range index, a non-existent column header title, or an invalid Column object is specified, an error occurs. |

## Version

Introduced in version 9
