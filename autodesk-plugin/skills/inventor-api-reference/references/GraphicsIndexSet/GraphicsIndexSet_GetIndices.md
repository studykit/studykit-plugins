# GraphicsIndexSet.GetIndices Method

Parent Object: [GraphicsIndexSet](../GraphicsIndexSet/GraphicsIndexSet.md)

## Description

Method that gets all of the indices of the set.

## Syntax

GraphicsIndexSet.**GetIndices**( ***IndexValues***() As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| IndexValues | Long | Output array of longs that contains the indices of the set. The array is a single dimension array. If the array has been declared undimensioned, this method will redimension its size to be able to contain the complete set of indices. If the array has been dimensioned, it must be large enough to contain the entire set of indices or an error will occur. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |