# TransientGeometry.CreateEllipticalArc2d Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new EllipticalArc2d object. The object created is a transient mathematical object and is not displayed graphically

## Syntax

TransientGeometry.**CreateEllipticalArc2d**( ***Center*** As [Point2d](../Point2d/Point2d.md), ***MajorAxis*** As [UnitVector2d](../UnitVector2d/UnitVector2d.md), ***MajorRadius*** As Double, ***MinorRadius*** As Double, ***StartAngle*** As Double, ***SweepAngle*** As Double ) As [EllipticalArc2d](../EllipticalArc2d/EllipticalArc2d.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Center | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the center of the elliptical arc. |
| MajorAxis | [UnitVector2d](../UnitVector2d/UnitVector2d.md) | Input UnitVector2d object that specifies the direction of the major axis of the elliptical arc. |
| MajorRadius | Double | Input Double that specifies the major radius of the elliptical arc. |
| MinorRadius | Double | Input Double that specifies the minor radius of the elliptical arc. |
| StartAngle | Double | Input Double that specifies start angle of the elliptical arc. The start angle is measured from the major axis vector. |
| SweepAngle | Double | Input Double that specifies the sweep angle from the start angle in a counterclockwise direction. |

## Version

Introduced in version 11
