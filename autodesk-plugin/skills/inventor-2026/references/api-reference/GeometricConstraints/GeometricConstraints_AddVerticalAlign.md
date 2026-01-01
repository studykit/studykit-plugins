# GeometricConstraints.AddVerticalAlign Method

Parent Object: [GeometricConstraints](../GeometricConstraints/GeometricConstraints.md)

## Description

Method that creates a new vertical alignment constraint between two sketch points. This causes the two points to align along the same vertical axis. This method will fail if the constraint overconstrains the sketch.

## Syntax

GeometricConstraints.**AddVerticalAlign**( ***PointOne*** As [SketchPoint](../SketchPoint/SketchPoint.md), ***PointTwo*** As [SketchPoint](../SketchPoint/SketchPoint.md) ) As [VerticalAlignConstraint](../VerticalAlignConstraint/VerticalAlignConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PointOne | [SketchPoint](../SketchPoint/SketchPoint.md) | Input SketchPoint entity. |
| PointTwo | [SketchPoint](../SketchPoint/SketchPoint.md) | Input SketchLine object. |

## Version

Introduced in version 5
