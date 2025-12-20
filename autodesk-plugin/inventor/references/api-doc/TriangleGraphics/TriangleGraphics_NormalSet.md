# TriangleGraphics.NormalSet Property

Parent Object: [TriangleGraphics](../TriangleGraphics/TriangleGraphics.md)

## Description

Gets and sets the GraphicsNormalSet associated with the set.

## Syntax

TriangleGraphics.**NormalSet**() As [GraphicsNormalSet](../GraphicsNormalSet/GraphicsNormalSet.md)

## Property Value

This is a read/write property whose value is a [GraphicsNormalSet](../GraphicsNormalSet/GraphicsNormalSet.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |
| [Client Graphics - Vertex Color by Z Height](../../sample-programs/GraphicsDataSets_CreateColorSet_Sample.md) | This sample demonstrates using client graphics and some other functions that help to support display control. It uses the currently active part and replaces the part display with a display where the part's color varies from blue to red where blue is assigned to the lowest Z portion of the part and red is assigned to the highest Z portion of the part. Areas in between are represented by a smooth blend of color from blue to red. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |