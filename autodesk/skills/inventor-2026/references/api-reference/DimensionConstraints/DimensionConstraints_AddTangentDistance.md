# DimensionConstraints.AddTangentDistance Method

Parent Object: [DimensionConstraints](../DimensionConstraints/DimensionConstraints.md)

## Description

Method that creates a new tangent distance dimension constraint between the two input entities. The input entities can consist of two circles or a line and a circle. Arcs can also be used in place of the circles.

## Remarks

The proximity point arguments are required whenever a circle or arc is input. This point specifies which of the two possible solutions is used when creating the constraint. The figure below illustrates two tangent distance constraints placed using the same input arguments except the proximity point for the smaller circle indicated the position closer to the large circle in one case and further away in the other.

![](../images/TangentDimConstraint3.png)

The General Dimension command allows you to dimension the difference in radius between two concentric circles. During interactive placement there is special behavior that makes the placement behave similar to that when placing a radius or diameter dimension. However, the command actually creates a TangentDistanceDimConstraint. By providing the appropriate input you can duplicate the result using the AddTangentDistance method. The result is shown below.

![](../images/ConcentricDimConstraint.png)

The picture below illustrates creating a tangent dimension constraint between a line and an arc. The 1.293 dia. dimension was placed by inputting the red line representing the center line and the red arc. It is defined to be a linear diameter style of dimension.

![](../images/TangentDimConstraint2.png)

## Syntax

DimensionConstraints.**AddTangentDistance**( ***EntityOne*** As [SketchEntity](../SketchEntity/SketchEntity.md), ***EntityTwo*** As [SketchEntity](../SketchEntity/SketchEntity.md), ***ProximityPointOne*** As [Point2d](../Point2d/Point2d.md), ***ProximityPointTwo*** As [Point2d](../Point2d/Point2d.md), ***TextPoint*** As [Point2d](../Point2d/Point2d.md), ***LinearDiameter*** As Boolean, [***Driven***] As Boolean ) As [TangentDistanceDimConstraint](../TangentDistanceDimConstraint/TangentDistanceDimConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | [SketchEntity](../SketchEntity/SketchEntity.md) | Input , SketchArc, or SketchLine object. Both EntityOne and EntityTwo cannot be sketch lines, at least one must be an arc or circle. |
| EntityTwo | [SketchEntity](../SketchEntity/SketchEntity.md) | Input , SketchArc, or SketchLine object. Both EntityOne and EntityTwo cannot be sketch lines, at least one must be an arc or circle. |
| ProximityPointOne | [Point2d](../Point2d/Point2d.md) | The supplied by this argument is used when EntityOne is a circle or arc. This point specifies which of the possible two tangent cases is used when creating the constraint. The closest tangent to the input point is used. If EntityOne is a line, this argument is ignored. |
| ProximityPointTwo | [Point2d](../Point2d/Point2d.md) | The supplied by this argument is used when EntityTwo is a circle or arc. This point specifies which of the possible two tangent cases is used when creating the constraint. The closest tangent to the input point is used. If EntityTwo is a line, this argument is ignored. |
| TextPoint | [Point2d](../Point2d/Point2d.md) | Input object that defines the position of the dimension text. |
| LinearDiameter | Boolean | In the case when either EntityOne or EntityTwo is a line, it is valid to specify that this constraint be placed as a linear diameter type of dimension. If neither EntityOne nor EntityTwo is a line, this argument is ignored. |
| Driven | Boolean | Optional input Boolean that specifies whether the dimension should be a driven or driving dimension. The default value is False, which causes a driving dimension constraint to be created. |

## Version

Introduced in version 5
