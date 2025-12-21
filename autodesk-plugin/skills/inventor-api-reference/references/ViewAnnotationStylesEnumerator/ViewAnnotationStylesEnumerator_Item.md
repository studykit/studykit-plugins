# ViewAnnotationStylesEnumerator.Item Property

Parent Object: [ViewAnnotationStylesEnumerator](../ViewAnnotationStylesEnumerator/ViewAnnotationStylesEnumerator.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

ViewAnnotationStylesEnumerator.**Item**( ***Index*** As Variant ) As [ViewAnnotationStyle](../ViewAnnotationStyle/ViewAnnotationStyle.md)

## Property Value

This is a read only property whose value is a [ViewAnnotationStyle](../ViewAnnotationStyle/ViewAnnotationStyle.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the ViewAnnotationStyle to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the ViewAnnotationStyle name. If an out of range index or a name of a non-existent ViewAnnotationStyle is provided, an error will occur. |

## Version

Introduced in version 2025.1
