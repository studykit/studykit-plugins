# GraphicsNormalSet.Add Method

Parent Object: [GraphicsNormalSet](../GraphicsNormalSet/GraphicsNormalSet.md)

## Description

Method that adds a new normal to the set.

## Syntax

GraphicsNormalSet.**Add**( ***Index*** As Long, ***Normal*** As [UnitVector](../UnitVector/UnitVector.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Specifies the position you want this normal to have within the set. All normals above the position will be shifted up to make room for this normal. Specifying any number greater than the current count of the set will cause the normal to become the last in the set. The normal set indices are one-based, meaning the first normal in the set has an index of one. |
| Normal | [UnitVector](../UnitVector/UnitVector.md) | Input object that specifies the normal to add to the set. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client Graphics - Triangle](../../sample-programs/GraphicsNode_AddTriangleFanGraphics_Sample.md) | This sample demonstrates the creation of client graphics triangles using triange fans and strips. It does this by drawing a cylinder. The end caps are triangle fans and the cylinder is made from a triangle strip. |

## Version

Introduced in version 5
