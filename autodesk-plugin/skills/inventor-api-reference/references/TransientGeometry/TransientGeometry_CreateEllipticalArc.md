# TransientGeometry.CreateEllipticalArc Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new EllipticalArc object. The object created is a transient mathematical object and is not displayed graphically

## Syntax

TransientGeometry.**CreateEllipticalArc**( ***Center*** As [Point](../Point/Point.md), ***MajorAxis*** As [UnitVector](../UnitVector/UnitVector.md), ***MinorAxis*** As [UnitVector](../UnitVector/UnitVector.md), ***MajorRadius*** As Double, ***MinorRadius*** As Double, ***StartAngle*** As Double, ***SweepAngle*** As Double ) As [EllipticalArc](../EllipticalArc/EllipticalArc.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Center | [Point](../Point/Point.md) | Input Point object that specifies the center of the elliptical arc. |
| MajorAxis | [UnitVector](../UnitVector/UnitVector.md) | Input UnitVector object that specifies the direction of the major axis of the elliptical arc. |
| MinorAxis | [UnitVector](../UnitVector/UnitVector.md) | Input UnitVector object that specifies the direction of the minor axis of the elliptical arc. |
| MajorRadius | Double | Input Double that specifies the major radius of the elliptical arc. |
| MinorRadius | Double | Input Double that specifies the minor radius of the elliptical arc. |
| StartAngle | Double | Input Double that specifies start angle of the elliptical arc. The start angle is measured from the major axis vector using the right\-hand rule about the axis vector. |
| SweepAngle | Double | Input Double that specifies the sweep angle from the start angle in a direction defined using the right\-hand rule about the axis vector. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |