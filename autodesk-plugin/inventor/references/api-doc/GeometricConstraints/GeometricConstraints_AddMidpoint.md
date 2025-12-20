# GeometricConstraints.AddMidpoint Method

Parent Object: [GeometricConstraints](../GeometricConstraints/GeometricConstraints.md)

## Description

Method that creates a new midpoint constraint between the point and line. This causes the input sketch point to be positioned at the midpoint of the input line. This method will fail if the constraint overconstrains the sketch.

## Syntax

GeometricConstraints.**AddMidpoint**( ***Point*** As [SketchPoint](../SketchPoint/SketchPoint.md), ***Line*** As [SketchLine](../SketchLine/SketchLine.md) ) As [MidpointConstraint](../MidpointConstraint/MidpointConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point | [SketchPoint](../SketchPoint/SketchPoint.md) | Input SketchPoint entity. |
| Line | [SketchLine](../SketchLine/SketchLine.md) | Input SketchLine object. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |