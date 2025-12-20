# GraphicsIndexSet.Add Method

Parent Object: [GraphicsIndexSet](../GraphicsIndexSet/GraphicsIndexSet.md)

## Description

Method that adds a new index to the set.

## Syntax

GraphicsIndexSet.**Add**( ***Index*** As Long, ***IndexValue*** As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Long that specifies the position you want this index to be within the set. All indices above the position will be shifted up to make room for this index. Specifying any number greater than the current count of the set will cause the index to become the last in the set. The index set indices are one-based. |
| IndexValue | Long | Input Long that specifies the index value. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client Graphics - Triangle](../../sample-programs/GraphicsNode_AddTriangleFanGraphics_Sample.md) | This sample demonstrates the creation of client graphics triangles using triange fans and strips. It does this by drawing a cylinder. The end caps are triangle fans and the cylinder is made from a triangle strip. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |