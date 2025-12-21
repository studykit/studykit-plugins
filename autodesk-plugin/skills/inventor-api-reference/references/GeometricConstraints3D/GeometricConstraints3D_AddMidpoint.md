# GeometricConstraints3D.AddMidpoint Method

Parent Object: [GeometricConstraints3D](../GeometricConstraints3D/GeometricConstraints3D.md)

## Description

Method that creates a new midpoint constraint between the input point and the midpoint of the line. This causes the input sketch point to be positioned at the midpoint of the \input line. This method will fail if the constraint overconstrains the sketch.

## Syntax

GeometricConstraints3D.**AddMidpoint**( ***Point*** As [SketchPoint3D](../SketchPoint3D/SketchPoint3D.md), ***Line*** As [SketchLine3D](../SketchLine3D/SketchLine3D.md) ) As [MidpointConstraint3D](../MidpointConstraint3D/MidpointConstraint3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point | [SketchPoint3D](../SketchPoint3D/SketchPoint3D.md) | Input SketchPoint3D object. |
| Line | [SketchLine3D](../SketchLine3D/SketchLine3D.md) | Input SketchLine3D object. |

## Version

Introduced in version 2009
