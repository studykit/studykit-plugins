# GeometricConstraints.AddCollinear Method

Parent Object: [GeometricConstraints](../GeometricConstraints/GeometricConstraints.md)

## Description

Method that creates a new collinear constraint between the two input sketch entities. Valid objects for input include lines, ellipses, and elliptical arcs. Either the major or minor axis of an ellipse is used, depending on the value of the EllipseMajorAxis input argument. When an ellipse is used, the specified axis of the ellipse will become collinear to the other entity. This method will fail if the constraint overconstrains the sketch.

## Syntax

GeometricConstraints.**AddCollinear**( ***EntityOne*** As [SketchEntity](../SketchEntity/SketchEntity.md), ***EntityTwo*** As [SketchEntity](../SketchEntity/SketchEntity.md), [***UseEllipseOneMajorAxis***] As Boolean, [***UseEllipseTwoMajorAxis***] As Boolean ) As [CollinearConstraint](../CollinearConstraint/CollinearConstraint.md)

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
