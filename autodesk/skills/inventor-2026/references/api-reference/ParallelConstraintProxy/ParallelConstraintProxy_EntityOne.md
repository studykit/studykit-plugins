# ParallelConstraintProxy.EntityOne Property

Parent Object: [ParallelConstraintProxy](../ParallelConstraintProxy/ParallelConstraintProxy.md)

## Description

Property that returns the sketch entity being constrained. This will be a line, ellipse, or elliptical arc. In the case where an elliptical entity is returned, the UsesEllipseOneMajorAxis property indicates if the parallel constraint is between the major or minor axis of the ellipse.

## Syntax

ParallelConstraintProxy.**EntityOne**() As [SketchEntity](../SketchEntity/SketchEntity.md)

## Property Value

This is a read only property whose value is a [SketchEntity](../SketchEntity/SketchEntity.md).

## Version

Introduced in version 6
