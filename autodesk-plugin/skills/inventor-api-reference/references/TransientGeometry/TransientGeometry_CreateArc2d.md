# TransientGeometry.CreateArc2d Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new Arc2d object. The object created is a transient mathematical object and is not displayed graphically.

## Syntax

TransientGeometry.**CreateArc2d**( ***Center*** As [Point2d](../Point2d/Point2d.md), ***Radius*** As Double, ***StartAngle*** As Double, ***SweepAngle*** As Double ) As [Arc2d](../Arc2d/Arc2d.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Center | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the center of the arc. Length units are always centimeters. |
| Radius | Double | Input Double that specifies the radius of the arc. |
| StartAngle | Double | Input Double that specifies the start angle of the arc. An angle of 0 is along the positive X axis of the sketch plane. |
| SweepAngle | Double | Input Double that specifies the sweep angle of the arc. The sweep direction is always counterclockwise. |

## Version

Introduced in version 11
