# BreakOperations.AddBySketch Method

Parent Object: [BreakOperations](../BreakOperations/BreakOperations.md)

## Description

Method that adds a break to a drawing view. The newly created BreakOperation object is returned.

## Syntax

BreakOperations.**AddBySketch**( ***Sketch*** As [DrawingSketch](../DrawingSketch/DrawingSketch.md), [***BreakStyle***] As [BreakStyleEnum](../BreakStyleEnum.md), [***DisplayLevel***] As Long, [***Gap***] As Double, [***NumberOfSymbols***] As Long, [***Reserved***] As Variant ) As [BreakOperation](../BreakOperation/BreakOperation.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Sketch | [DrawingSketch](../DrawingSketch/DrawingSketch.md) | Input DrawingSketch that specifies the sketch with sketch lines as the break lines to break the drawing view. The DrawingSketch should contain two vertical or horizontal sketch lines |
| BreakStyle | [BreakStyleEnum](../BreakStyleEnum.md) | Optional input BreakStyleEnum that specifies the break style. Valid values are kRectangularBreakStyle and kStructuralBreakStyle. If not specified, a rectangular style break is created. |
| DisplayLevel | Long | Optional input Long that specifies the appearance of the break lines. Valid range of values is 1 through 10. For rectangular break style, this value controls the quantity or pitch of break edges displayed. For structural break style, this value controls amplitude of break line. If not specified, a value of 5 is used.   This is an optional argument whose default value is 5. |
| Gap | Double | Optional input Double that specifies the gap (in centimeters) between the break lines. If not specified, a gap value is automatically calculated based on the view size.   This is an optional argument whose default value is 0.0. |
| NumberOfSymbols | Long | Optional input Long that specifies the number of break symbols to use for a structural style break. Valid values are 1, 2 and 3. This argument is not applicable and is ignored for rectangular style breaks. If not specified, a value of 1 is assumed.   This is an optional argument whose default value is 1. |
| Reserved | Variant | Reserved for future use.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create BreakOpertion by Sketch Sample](../../sample-programs/CreateBreakOpertionBySketchSample_Sample.md) | This sample demonstrates how to create a break operation using a sketch. |

## Version

Introduced in version 2026

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |