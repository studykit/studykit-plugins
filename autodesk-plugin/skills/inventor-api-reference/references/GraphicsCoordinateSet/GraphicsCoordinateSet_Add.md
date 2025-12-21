# GraphicsCoordinateSet.Add Method

Parent Object: [GraphicsCoordinateSet](../GraphicsCoordinateSet/GraphicsCoordinateSet.md)

## Description

Method that adds a single coordinate to the set.

## Syntax

GraphicsCoordinateSet.**Add**( ***Index*** As Long, ***Coordinate*** As [Point](../Point/Point.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Specifies the index you want this coordinate to be within the set. All coordinates above the Index will be shifted up to make room for this index. Specifying any number greater than the current count of the set will cause the coordinate to become the last in the set. The coordinate set indices are one-based. |
| Coordinate | [Point](../Point/Point.md) | Input object that specifies the coordinate to add. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |