# GraphicsTextureCoordinateSet.Add Method

Parent Object: [GraphicsTextureCoordinateSet](../GraphicsTextureCoordinateSet/GraphicsTextureCoordinateSet.md)

## Description

Method that adds a single coordinate to the set.

## Syntax

GraphicsTextureCoordinateSet.**Add**( ***Index*** As Long, ***Coordinate*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Specifies the index you want this coordinate to be within the set. All coordinates above the Index will be shifted up to make room for this index. Specifying any number greater than the current count of the set will cause the coordinate to become the last in the set. The coordinate set indices are one-based. |
| Coordinate | Variant | Input Double that specifies the value of the coordinate to add. The input is currently limited to double values. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |