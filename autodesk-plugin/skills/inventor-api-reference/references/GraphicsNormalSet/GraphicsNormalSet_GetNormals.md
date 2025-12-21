# GraphicsNormalSet.GetNormals Method

Parent Object: [GraphicsNormalSet](../GraphicsNormalSet/GraphicsNormalSet.md)

## Description

Method that gets all of the normals of the set.

## Syntax

GraphicsNormalSet.**GetNormals**( ***Normals***() As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Normals | Double | Input/output array of Doubles that contains the x-y-z values of the normals. The array is a single dimension array containing sequential x, y, and z values. If the array has been declared undimensioned, this method will redimension its size to be able to contain the complete set of normals. If the array has been dimensioned, it must be large enough to contain the entire set of normals or an error will occur. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |