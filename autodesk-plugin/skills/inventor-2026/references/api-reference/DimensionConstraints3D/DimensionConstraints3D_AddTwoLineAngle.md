# DimensionConstraints3D.AddTwoLineAngle Method

Parent Object: [DimensionConstraints3D](../DimensionConstraints3D/DimensionConstraints3D.md)

## Description

Method that creates a new angular dimension constraint between two 3D sketch lines. This method will fail if the two input 3D sketch lines that need to be constrained are not co-planar. This method will also fail in the case where a driving dimension is specified and it will overconstrain the sketch.

## Syntax

DimensionConstraints3D.**AddTwoLineAngle**( ***LineOne*** As [SketchLine3D](../SketchLine3D/SketchLine3D.md), ***LineTwo*** As [SketchLine3D](../SketchLine3D/SketchLine3D.md), [***TextPoint***] As Variant, [***Driven***] As Boolean ) As [TwoLineAngleDimConstraint3D](../TwoLineAngleDimConstraint3D/TwoLineAngleDimConstraint3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| LineOne | [SketchLine3D](../SketchLine3D/SketchLine3D.md) | Object that defines the first 3D sketch line being constrained. |
| LineTwo | [SketchLine3D](../SketchLine3D/SketchLine3D.md) | Object that defines the second 3D sketch line being constrained. |
| TextPoint | Variant | Point object that defines the position of the dimension text. The dimension text will always be placed on a particular dimension plane the orientation of which will be automatically determined based on the input plane and sketch point to which the dimension is being applied. The dimension plane is a transient geometric plane which is only used to define the placement plane for the dimension text and does not have a graphical representation. If no input is specified for the position of the dimension text, a default position on the dimension plane will be calculated and used to place the dimension text. If a valid point for the dimension text is specified, then either of the following conditions will apply: \* If the specified point already lies on the dimension plane, then this point will be directly used to place the dimension text. \* If the specified point does not lie on the dimension plane, it will be projected onto the dimension plane. Therefore, the resultant placement position for the dimension text will be different from the specified one. The GetDimensionPlane method of the DimensionConstraints3D object can be used to get the dimension plane object which provides access to the dimension plane geometry. |
| Driven | Boolean | Specifies whether the dimension should be a driven or driving dimension. The default value is False, which causes a driving dimension constraint to be created.   This is an optional argument whose default value is False. |

## Version

Introduced in version 11
