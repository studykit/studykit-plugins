# EllipticalArc2d.PutEllipticalArcData Method

Parent Object: [EllipticalArc2d](../EllipticalArc2d/EllipticalArc2d.md)

## Description

Method that sets the data defining this elliptical arc.

## Syntax

EllipticalArc2d.**PutEllipticalArcData**( ***Center***() As Double, ***MajorAxis***() As Double, ***MajorRadius*** As Double, ***MinorRadius*** As Double, ***StartAngle*** As Double, ***SweepAngle*** As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Center | Double | Input/output Double that specifies the elliptical arc's center. |
| MajorAxis | Double | Input/output Double that specifies major axis. |
| MajorRadius | Double | Input Double that specifies major radius. |
| MinorRadius | Double | Input Double that specifies the minor radius. |
| StartAngle | Double | Input Double that specifies the elliptical arc's start angle. This angle is an elliptical angle, not a circular angle, unlike the user interface which uses circular angles in all cases. To convert from an elliptical angle to a circular angle CircAngle = atn( tan(EllipAngle) \* MinorRadius / MajorRadius ) To convert from a circular angle to an elliptical angle EllipAngle = atn( tan(CircAngle) \* MajorRadius / MinorRadius ) |
| SweepAngle | Double | Input Double that specifies the elliptical arc's sweep angle. This angle is an elliptical angle, not a circular angle, unlike the user interface which uses circular angles in all cases. To convert from an elliptical angle to a circular angle CircAngle = atn( tan(EllipAngle) \* MinorRadius / MajorRadius ) To convert from a circular angle to an elliptical angle EllipAngle = atn( tan(CircAngle) \* MajorRadius / MinorRadius ) |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |