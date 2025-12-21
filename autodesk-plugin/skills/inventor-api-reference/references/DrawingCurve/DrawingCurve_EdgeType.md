# DrawingCurve.EdgeType Property

Parent Object: [DrawingCurve](../DrawingCurve/DrawingCurve.md)

## Description

Property that returns the edge type of this curve. Possible return values are kThreadEdge, kBendUpEdge, kBendDownEdge, kBendExtentEdge, kPunchDownEdge, kPunchUpEdge, kTangentEdge, kContourRollEdge, and kUnknownEdge.

## Syntax

DrawingCurve.**EdgeType**() As [DrawingEdgeTypeEnum](../DrawingEdgeTypeEnum.md)

## Property Value

This is a read only property whose value is a [DrawingEdgeTypeEnum](../DrawingEdgeTypeEnum.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create bend note](../../sample-programs/BendNotes_Add_Sample.md) | This sample demonstrates the creation of a bend note on the drawing view of a flat pattern. |
| [Create thread note](../../sample-programs/HoleThreadNotes_Add_Sample.md) | This sample demonstrates the creation of a thread note on a drawing view. |
| [create punch note](../../sample-programs/PunchNotes_Add_Sample.md) | This sample demonstrates the creation of a punch note on the drawing view of a flat pattern. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |