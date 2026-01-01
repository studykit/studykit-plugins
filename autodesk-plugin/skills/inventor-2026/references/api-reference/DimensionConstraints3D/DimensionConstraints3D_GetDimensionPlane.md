# DimensionConstraints3D.GetDimensionPlane Method

Parent Object: [DimensionConstraints3D](../DimensionConstraints3D/DimensionConstraints3D.md)

## Description

Method that gets the transient dimension plane used to place and position the dimension text when a dimension constraint is applied to the specified input entities.

## Remarks

The dimension plane is a transient geometric plane which is only used to define the placement plane for the dimension text and does not have a graphical representation. The orientation of the dimension plane will be automatically determined using the sketch entities when they are dimensioned. The dimension text will always be placed on this dimension plane. This method can be used to determine this dimension plane prior to actually creating the dimension constraint. The geometric information about the dimension plane could be used to calculate a 3D point that lies on the plane. This point can then be supplied as input for the position for the dimension text when creating the dimension constraint in which case the resultant position of the dimension text will be the same as the specified input placement point. On the other hand, if a placement point that does not lie on the dimension plane is specified as the position for the dimension text, it will be projected onto the dimension plane and the dimension text will be placed at this projected point. The following table shows the combination of the types of input objects that can be used to determine the dimension plane for the various dimension constraints. This combination matches the input types that will be supplied to actually create the corresponding dimension constraint.

Dimension Constraint Objects in collection ------------------------------------- ------------------------- LineLengthDimConstraint3D SketchLine3D PointAndPlaneDistanceDimConstraint3D SketchPoint3D and Face (planar) or SketchPoint3D and WorkPlane TwoLineAngleDimConstraint3D SketchLine3D and SketchLine3D TwoPointDistanceDimConstraint3D SketchPoint3D and SketchPoint3D or SketchPoint3D and Vertex or SketchPoint3D and WorkPoint

The collection must contain one of the combination of objects specified in the above table, otherwise the dimension plane cannot be determined.

## Syntax

DimensionConstraints3D.**GetDimensionPlane**( ***Entities*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md) ) As [Plane](../Plane/Plane.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entities | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | ObjectCollection that contains the entity objects that represents the entities for which the dimension plane has to be determined. The objects in this collection should normally contain the same objects that would be supplied as inputs to create a dimension constraint. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a 3D sketch dimension](../../sample-programs/DimensionConstraints3D_AddTwoPointDistance_Sample.md) | This sample demonstrates the creation of a 3d sketch line and a dimension between the start and the end points of the line. |

## Version

Introduced in version 11
