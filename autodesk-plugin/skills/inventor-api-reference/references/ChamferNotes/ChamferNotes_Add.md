# ChamferNotes.Add Method

Parent Object: [ChamferNotes](../ChamferNotes/ChamferNotes.md)

## Description

Method that creates a chamfer note positioned at the specified point on the sheet.

## Syntax

ChamferNotes.**Add**( ***Position*** As [Point2d](../Point2d/Point2d.md), ***ChamferEdgeOne*** As Object, ***ChamferEdgeTwo*** As Object, [***DimensionStyle***] As Variant ) As [ChamferNote](../ChamferNote/ChamferNote.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Position | [Point2d](../Point2d/Point2d.md) | Input Point2d that specifies the position of the chamfer note on the sheet. |
| ChamferEdgeOne | Object | Input object that specifies the first chamfer edge. This can either be a linear DrawingCurve object or a SketchLine object from a sheet sketch. Use the corresponding DrawingCurve objects for view sketch and model sketch entities. The leader of the chamfer note will point to the center of entity. |
| ChamferEdgeTwo | Object | Input object that specifies the second chamfer edge. This can either be a linear DrawingCurve object or a SketchLine object from a sheet sketch. Use the corresponding DrawingCurve objects for view sketch and model sketch entities. This object must be connected to the first chamfer edge and at an angle other than 90 degrees, else the method will fail. |
| DimensionStyle | Variant | Optional input Variant that specifies which dimension style to use for the note. The dimension style can be specified by providing the name of an existing style or by supplying a DimensionStyle object. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |