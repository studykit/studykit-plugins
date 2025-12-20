# TransientGeometry.CreateEllipseFull Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new EllipseFull object. The object created is a transient mathematical object and is not displayed graphically.

## Syntax

TransientGeometry.**CreateEllipseFull**( ***Center*** As [Point](../Point/Point.md), ***Normal*** As [UnitVector](../UnitVector/UnitVector.md), ***MajorAxisVector*** As [Vector](../Vector/Vector.md), ***MinorMajorRatio*** As Double ) As [EllipseFull](../EllipseFull/EllipseFull.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Center | [Point](../Point/Point.md) | Input Point object that specifies the center of the ellipse. |
| Normal | [UnitVector](../UnitVector/UnitVector.md) | Input UnitVector object that specifies the axis of the ellipse. The axis extends out of the ellipse. |
| MajorAxisVector | [Vector](../Vector/Vector.md) | Input Vector object that specifies the direction of the major axis of the ellipse. |
| MinorMajorRatio | Double | Input Double that specifies the ratio of the minor and major axes of the ellipse. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |