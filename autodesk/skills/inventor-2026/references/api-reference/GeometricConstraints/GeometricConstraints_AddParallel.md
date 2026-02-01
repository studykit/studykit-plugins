# GeometricConstraints.AddParallel Method

Parent Object: [GeometricConstraints](../GeometricConstraints/GeometricConstraints.md)

## Description

Method that creates a new parallel constraint between the two input sketch entities. Valid objects for input include lines and ellipses. Either the major or minor axis of an ellipse is used depending on the values of UseEllipseMajorAxis input arguments. When an ellipse is used, the specified axis of the ellipse will become parallel to the other entity. This method will fail if the constraint overconstrains the sketch.

## Syntax

GeometricConstraints.**AddParallel**( ***EntityOne*** As [SketchEntity](../SketchEntity/SketchEntity.md), ***EntityTwo*** As [SketchEntity](../SketchEntity/SketchEntity.md), [***UseEllipseOneMajorAxis***] As Boolean, [***UseEllipseTwoMajorAxis***] As Boolean ) As [ParallelConstraint](../ParallelConstraint/ParallelConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | [SketchEntity](../SketchEntity/SketchEntity.md) | Input sketch entity. Must be a line, ellipse, or elliptical arc. |
| EntityTwo | [SketchEntity](../SketchEntity/SketchEntity.md) | Input sketch entity. Must be a line, ellipse, or elliptical arc. |
| UseEllipseOneMajorAxis | Boolean | Optional Boolean that specifies whether to use the major or minor axis for the ellipse supplied in the EntityOne argument. This argument only applies when the input entity is an ellipse or elliptical arc. Inputting True results in the constraint being applied to the major axis. This value is ignored when a line is supplied as the EntityOne argument. |
| UseEllipseTwoMajorAxis | Boolean | Optional Boolean that specifies whether to use the major or minor axis for the ellipse supplied in the EntityTwo argument. This argument only applies when the input entity is an ellipse or elliptical arc. Inputting True results in the constraint being applied to the major axis. This value is ignored when a line is supplied as the EntityTwo argument.   This is an optional argument whose default value is True. |

## Version

Introduced in version 5
