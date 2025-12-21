# DimensionConstraints3D.AddTwoPointDistance Method

Parent Object: [DimensionConstraints3D](../DimensionConstraints3D/DimensionConstraints3D.md)

## Description

Method that creates a new linear dimension constraint between a 3D sketch point and another 3D sketch point, vertex or workpoint. This method will fail in the case where a driving dimension is specified and it will overconstrain the sketch.

## Remarks

The constraint can currently be applied between: \* two 3D sketch points \* a 3D sketch point and a vertex \* a 3D sketch point and a workpoint

## Syntax

DimensionConstraints3D.**AddTwoPointDistance**( ***PointOne*** As Object, ***PointTwo*** As Object, [***TextPoint***] As Variant, [***Driven***] As Boolean ) As [TwoPointDistanceDimConstraint3D](../TwoPointDistanceDimConstraint3D/TwoPointDistanceDimConstraint3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PointOne | Object | SketchPoint3D, Vertex or WorkPoint object that defines the first point being constrained. |
| PointTwo | Object | SketchPoint3D, Vertex or WorkPoint object that defines the second point being constrained. At least one of the input points (PointOne or PointTwo) for the dimension constraint must be a SketchPoint3D object. If a 3D sketch point is specified for either PointOne or PointTwo and a vertex or workpoint is specified for the other point, then a 3D sketch point will be created at the specified vertex or workpoint and then the constraint will be applied between the two 3D sketch points. |
| TextPoint | Variant | Point object that defines the position of the dimension text. The dimension text will always be placed on a particular dimension plane the orientation of which will be automatically determined based on the input plane and sketch point to which the dimension is being applied. The dimension plane is a transient geometric plane which is only used to define the placement plane for the dimension text and does not have a graphical representation. If no input is specified for the position of the dimension text, a default position on the dimension plane will be calculated and used to place the dimension text. If a valid point for the dimension text is specified, then either of the following conditions will apply: \* If the specified point already lies on the dimension plane, then this point will be directly used to place the dimension text. \* If the specified point does not lie on the dimension plane, it will be projected onto the dimension plane. Therefore, the resultant placement position for the dimension text will be different from the specified one. The GetDimensionPlane method of the DimensionConstraints3D object can be used to get the dimension plane object which provides access to the dimension plane geometry. |
| Driven | Boolean | Specifies whether the dimension should be a driven or driving dimension. The default value is False, which causes a driving dimension constraint to be created.   This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a 3D sketch dimension](../../sample-programs/DimensionConstraints3D_AddTwoPointDistance_Sample.md) | This sample demonstrates the creation of a 3d sketch line and a dimension between the start and the end points of the line. |

## Version

Introduced in version 11
