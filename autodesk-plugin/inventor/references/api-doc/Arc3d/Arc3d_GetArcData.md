# Arc3d.GetArcData Method

Parent Object: [Arc3d](../Arc3d/Arc3d.md)

## Description

Get the data defining this arc.

## Syntax

Arc3d.**GetArcData**( ***Center***() As Double, ***AxisVector***() As Double, ***RefVector***() As Double, ***Radius*** As Double, ***StartAngle*** As Double, ***SweepAngle*** As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Center | Double | Input/output Double that specifies the arc's center. |
| AxisVector | Double | Input/output Double that specifies axis vector. |
| RefVector | Double | Input/output Double that specifies the reference vector. |
| Radius | Double | Output Double that specifies the radius of the arc. |
| StartAngle | Double | Input Double that specifies the elliptical arc's start angle. |
| SweepAngle | Double | Output Double that specifies the arc's sweep angle. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |