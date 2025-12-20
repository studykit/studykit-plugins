# Plane.IntersectWithLine Method

Parent Object: [Plane](../Plane/Plane.md)

## Description

Compute the intersection point of this Plane and the specified Line. If the Plane and the Line are parallel, this method will fail.

## Syntax

Plane.**IntersectWithLine**( ***Line*** As Object, [***Tolerance***] As Double ) As [Point](../Point/Point.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Line | Object | Input object that represents a line. This object can be a Line or LineSegment object. |
| Tolerance | Double | Input Double that specifies the tolerance. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |