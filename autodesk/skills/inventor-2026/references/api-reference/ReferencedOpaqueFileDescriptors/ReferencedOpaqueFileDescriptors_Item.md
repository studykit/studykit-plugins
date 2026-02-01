# ReferencedOpaqueFileDescriptors.Item Property

Parent Object: [ReferencedOpaqueFileDescriptors](../ReferencedOpaqueFileDescriptors/ReferencedOpaqueFileDescriptors.md)

## Description

Allows integer-indexed access to items in the collection.

## Syntax

ReferencedOpaqueFileDescriptors.**Item**( ***Index*** As Long ) As [ReferencedOpaqueFileDescriptor](../ReferencedOpaqueFileDescriptor/ReferencedOpaqueFileDescriptor.md)

## Property Value

This is a read only property whose value is a [ReferencedOpaqueFileDescriptor](../ReferencedOpaqueFileDescriptor/ReferencedOpaqueFileDescriptor.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Variant value that specifies the ReferencedOpaqueFileDescriptor to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the full file name. If an out of range index or a name of a non-existent ReferencedOpaqueFileDescriptor is provided, an error will occur. |

## Version

Introduced in version 2017
