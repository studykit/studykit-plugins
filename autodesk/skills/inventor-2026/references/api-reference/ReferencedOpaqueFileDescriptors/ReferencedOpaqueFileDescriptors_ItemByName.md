# ReferencedOpaqueFileDescriptors.ItemByName Property

Parent Object: [ReferencedOpaqueFileDescriptors](../ReferencedOpaqueFileDescriptors/ReferencedOpaqueFileDescriptors.md)

## Description

Allows string-indexed access to items in the collection. Usually found when this ability has been added to an pre-existing collection.

## Syntax

ReferencedOpaqueFileDescriptors.**ItemByName**( ***Name*** As String ) As [ReferencedOpaqueFileDescriptor](../ReferencedOpaqueFileDescriptor/ReferencedOpaqueFileDescriptor.md)

## Property Value

This is a read only property whose value is a [ReferencedOpaqueFileDescriptor](../ReferencedOpaqueFileDescriptor/ReferencedOpaqueFileDescriptor.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Input String value that specifies the full file name of ReferencedOpaqueFileDescriptor. If a name of a non-existent ReferencedOpaqueFileDescriptor is provided, an error will occur. |

## Version

Introduced in version 2017
