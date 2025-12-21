# BendNotes.Add Method

Parent Object: [BendNotes](../BendNotes/BendNotes.md)

## Description

Method that creates a bend note based on the input bend edge on the sheet. The initial placement of the bend note will be along the bend edge without a leader.

## Syntax

BendNotes.**Add**( ***BendEdge*** As [DrawingCurve](../DrawingCurve/DrawingCurve.md), [***DimensionStyle***] As Variant ) As [BendNote](../BendNote/BendNote.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BendEdge | [DrawingCurve](../DrawingCurve/DrawingCurve.md) | Input DrawingCurve object that specifies the bend edge to create the note for. If the DrawingCurve does not represent a bend edge, the method returns an error. |
| DimensionStyle | Variant | Optional input Variant that specifies which dimension style to use for the note. The dimension style can be specified by providing the name of an existing style or by supplying a DimensionStyle object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create bend note](../../sample-programs/BendNotes_Add_Sample.md) | This sample demonstrates the creation of a bend note on the drawing view of a flat pattern. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |