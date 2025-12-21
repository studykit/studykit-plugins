# MarkStylesEnumerator.Item Property

Parent Object: [MarkStylesEnumerator](../MarkStylesEnumerator/MarkStylesEnumerator.md)

## Description

Allows integer-indexed access to items in the collection.

## Syntax

MarkStylesEnumerator.**Item**( ***Index*** As Variant ) As [MarkStyle](../MarkStyle/MarkStyle.md)

## Property Value

This is a read only property whose value is a [MarkStyle](../MarkStyle/MarkStyle.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the MarkStyle to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the MarkStyle name. If an out of range index or a name of a non-existent MarkStyle is provided, an error will occur. |

## Version

Introduced in version 2023
