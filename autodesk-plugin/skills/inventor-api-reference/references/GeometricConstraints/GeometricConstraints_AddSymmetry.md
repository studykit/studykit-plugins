# GeometricConstraints.AddSymmetry Method

Parent Object: [GeometricConstraints](../GeometricConstraints/GeometricConstraints.md)

## Description

Method that creates a new symmetry constraint between the two input entities about the specified line. The two input entities must be of the same type. This method will fail if the constraint overconstrains the sketch.

## Syntax

GeometricConstraints.**AddSymmetry**( ***EntityOne*** As [SketchEntity](../SketchEntity/SketchEntity.md), ***EntityTwo*** As [SketchEntity](../SketchEntity/SketchEntity.md), ***SymmetryAxis*** As [SketchLine](../SketchLine/SketchLine.md) ) As [SymmetryConstraint](../SymmetryConstraint/SymmetryConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | [SketchEntity](../SketchEntity/SketchEntity.md) | Input entity that is to be symmetric. Must be the same type as EntityTwo. |
| EntityTwo | [SketchEntity](../SketchEntity/SketchEntity.md) | Input entity that is to be symmetric. Must be the same type as EntityOne. |
| SymmetryAxis | [SketchLine](../SketchLine/SketchLine.md) | Input object that defines the axis of symmetry. |

## Version

Introduced in version 5
