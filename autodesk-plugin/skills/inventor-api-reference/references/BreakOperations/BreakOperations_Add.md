# BreakOperations.Add Method

Parent Object: [BreakOperations](../BreakOperations/BreakOperations.md)

## Description

Method that adds a break to a drawing view. The newly created BreakOperation object is returned.

## Syntax

BreakOperations.**Add**( ***Orientation*** As [BreakOrientationEnum](../BreakOrientationEnum.md), ***StartPoint*** As [Point2d](../Point2d/Point2d.md), ***EndPoint*** As [Point2d](../Point2d/Point2d.md), [***BreakStyle***] As [BreakStyleEnum](../BreakStyleEnum.md), [***DisplayLevel***] As Long, [***Gap***] As Double, [***NumberOfSymbols***] As Long, [***PropagateToParentView***] As Boolean ) As [BreakOperation](../BreakOperation/BreakOperation.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Orientation | [BreakOrientationEnum](../BreakOrientationEnum.md) | Input BreakOrientationEnum that specifies whether the orientation of the break is horizontal or vertical. Valid values are kHorizontalBreakOrientation and kVerticalBreakOrientation. |
| StartPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the start point of the break in sheet space. For a horizontal break orientation, only the 'x' component of the point is used and the 'y' component is ignored. For a vertical break, only the 'y' component of the point is used and the 'x' component is ignored. |
| EndPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the end point of the break in sheet space. For a horizontal break orientation, only the 'x' component of the point is used and the 'y' component is ignored. For a vertical break, only the 'y' component of the point is used and the 'x' component is ignored. |
| BreakStyle | [BreakStyleEnum](../BreakStyleEnum.md) | Optional input BreakStyleEnum that specifies the break style. Valid values are kRectangularBreakStyle and kStructuralBreakStyle. If not specified, a rectangular style break is created. |
| DisplayLevel | Long | Optional input Long that specifies the appearance of the break lines. Valid range of values is 1 through10. For rectangular break style, this value controls the quantity or pitch of break edges displayed. For structural break style, this value controls amplitude of break line. If not specified, a value of 5 is used.   This is an optional argument whose default value is 5. |
| Gap | Double | Optional input Double that specifies the gap (in centimeters) between the break lines. If not specified, a gap value is automatically calculated based on the view size.   This is an optional argument whose default value is 0.0. |
| NumberOfSymbols | Long | Optional input Long that specifies the number of break symbols to use for a structural style break. Valid values are 1, 2 and 3. This argument is not applicable and is ignored for rectangular style breaks. If not specified, a value of 1 is assumed.   This is an optional argument whose default value is 1. |
| PropagateToParentView | Boolean | Optional input Boolean that specifies whether to apply this break to the parent view as well. This is not applicable in all situations and is ignored if not applicable. The default value is False.   This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creation of a break operation in a drawing view](../../sample-programs/BreakOperations_Add_Sample.md) | Demonstrates the creation of a break operation. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |