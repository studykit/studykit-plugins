# DimensionConstraints.AddDiameter Method

Parent Object: [DimensionConstraints](../DimensionConstraints/DimensionConstraints.md)

## Description

Method that creates a new diameter dimension constraint on the input circle or arc.

## Remarks

This method will fail in the case where a driving dimension is specified and it will overconstrain the sketch. The picture below illustrates the result of adding a diameter dimension constraint.

![](../images/DiameterDimConstraint.png)

## Syntax

DimensionConstraints.**AddDiameter**( ***Entity*** As [SketchEntity](../SketchEntity/SketchEntity.md), ***TextPoint*** As [Point2d](../Point2d/Point2d.md), [***Driven***] As Boolean ) As [DiameterDimConstraint](../DiameterDimConstraint/DiameterDimConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entity | [SketchEntity](../SketchEntity/SketchEntity.md) | Input or SketchArc object. |
| TextPoint | [Point2d](../Point2d/Point2d.md) | Input object that defines the position of the dimension text. |
| Driven | Boolean | Optional input Boolean that specifies whether the dimension should be a driven or driving dimension. The default value is False, which causes a driving dimension constraint to be created. |

## Version

Introduced in version 5
