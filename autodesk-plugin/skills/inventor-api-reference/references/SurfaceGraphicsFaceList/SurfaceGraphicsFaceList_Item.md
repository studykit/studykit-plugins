# SurfaceGraphicsFaceList.Item Property

Parent Object: [SurfaceGraphicsFaceList](../SurfaceGraphicsFaceList/SurfaceGraphicsFaceList.md)

## Description

Returns a SurfaeGraphicsFace object.

## Syntax

SurfaceGraphicsFaceList.**Item**( ***Index*** As Variant ) As [SurfaceGraphicsFace](../SurfaceGraphicsFace/SurfaceGraphicsFace.md)

## Property Value

This is a read only property whose value is a [SurfaceGraphicsFace](../SurfaceGraphicsFace/SurfaceGraphicsFace.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Specifies which SurfaceGraphicsFace object to return. This can be a Long, which specifies the index in the list, or it can be the Face object referenced by a SurfaceGraphicsFace object. The property will fail in the case where an Index is provided that does not identify an existing SurfaceGraphicsFace object. |

## Version

Introduced in version 2009
