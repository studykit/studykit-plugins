# GraphicsCoordinateSet.GetCoordinates Method

Parent Object: [GraphicsCoordinateSet](../GraphicsCoordinateSet/GraphicsCoordinateSet.md)

## Description

Method that gets all of the coordinates of the set.

## Syntax

GraphicsCoordinateSet.**GetCoordinates**( ***Coordinates***() As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Coordinates | Double | Input/output array of Doubles that contains the x-y-z value of the coordinates. The array is a single dimension array containing sequential x, y, and z values. If the array has been declared undimensioned, this method will redimension its size to be able to contain the complete set of coordinates. If the array has been dimensioned, it must be large enough to contain the entire set of coordinates or an error will occur. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |