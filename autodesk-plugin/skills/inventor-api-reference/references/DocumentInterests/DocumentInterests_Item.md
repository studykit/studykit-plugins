# DocumentInterests.Item Property

Parent Object: [DocumentInterests](../DocumentInterests/DocumentInterests.md)

## Description

Returns the specified DocumentInterest object from the collection

## Syntax

DocumentInterests.**Item**( ***Index*** As Variant ) As [DocumentInterest](../DocumentInterest/DocumentInterest.md)

## Property Value

This is a read only property whose value is a [DocumentInterest](../DocumentInterest/DocumentInterest.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the DocumentInterest to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the ClientId associated with the DocumentInterest, or it can be the a string indicating the Name of the DocumentInterest. If an out of range index or a ClientId/Name of a non-existent DocumentInterest is provided, an error will occur. |

## Version

Introduced in version 2008
