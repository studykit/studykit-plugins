# WorkPlanes Object

## Description

The WorkPlanes collection object provides access to all of the  objects in the parent document and provides methods to create new work planes.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddByLineAndTangent](../WorkPlanes/WorkPlanes_AddByLineAndTangent.md) | Method that creates a new work plane through the input line and tangent to the input surface. This method is not currently supported when creating a work plane within an assembly. |
| [AddByLinePlaneAndAngle](../WorkPlanes/WorkPlanes_AddByLinePlaneAndAngle.md) | Method that creates a new work plane through the input line at the specified angle from the input plane. This method is not currently supported when creating a work plane within an assembly. |
| [AddByNormalToCurve](../WorkPlanes/WorkPlanes_AddByNormalToCurve.md) | Method that creates a new work plane that passes through the point and is normal to the input curve. The point must lie on the curve, as described below. This method is not currently supported when creating a work plane within an assembly. |
| [AddByPlaneAndOffset](../WorkPlanes/WorkPlanes_AddByPlaneAndOffset.md) | Method that creates a new work plane that is parallel to the input plane at a specified distance in the specified direction. This method is not currently supported when creating a work plane within an assembly. |
| [AddByPlaneAndPoint](../WorkPlanes/WorkPlanes_AddByPlaneAndPoint.md) | Method that creates a new work plane that is parallel to the input plane and passes through the input point. This method is not currently supported when creating a work plane within an assembly. |
| [AddByPlaneAndTangent](../WorkPlanes/WorkPlanes_AddByPlaneAndTangent.md) | Method that creates a new work plane that is parallel to the input plane and tangent to the input surface. Valid geometry for the face includes cylinders, cones, and spheres. This method is not currently supported when creating a work plane within an assembly. |
| [AddByPointAndTangent](../WorkPlanes/WorkPlanes_AddByPointAndTangent.md) | Method that creates a new work plane through the input point and tangent to the input surface. The input point must lie on the input surface. This method is not currently supported when creating a work plane within an assembly. |
| [AddByThreePoints](../WorkPlanes/WorkPlanes_AddByThreePoints.md) | Method that creates a new work plane based on the three input points. The three input points must be unique non-coincident points. Point1 to Point2 defines the positive X axis and Point3 defines the positive Y direction. This method is not currently supported when creating a work plane within an assembly. |
| [AddByTorusMidPlane](../WorkPlanes/WorkPlanes_AddByTorusMidPlane.md) | Method that creates a new work plane at the mid-plane of the torus specified by the input face. This method is not currently supported when creating a work plane within an assembly. |
| [AddByTwoLines](../WorkPlanes/WorkPlanes_AddByTwoLines.md) | Method that creates a new work plane based on the two input lines. Line1 defines the X axis. If the two lines are not in the same plane, the plane is calculated by crossing the vectors defined by Line1 and Line2. This method is not currently supported when creating a work plane within an assembly. |
| [AddByTwoPlanes](../WorkPlanes/WorkPlanes_AddByTwoPlanes.md) | Creates a new work plane that bisects the two input planes. This method is not currently supported when creating a work plane within an assembly. |
| [AddFixed](../WorkPlanes/WorkPlanes_AddFixed.md) | Method that creates a new work plane at the position and orientation defined by the point and X and Y axis vectors. When used to create a work plane within an assembly the resulting work plane will return an AssemblyWorkPlaneDef definition. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../WorkPlanes/WorkPlanes_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../WorkPlanes/WorkPlanes_Count.md) | Property that returns the number of items in this collection. |
| [Item](../WorkPlanes/WorkPlanes_Item.md) | Returns the specified WorkPlane object from the collection. This is the default property of the WorkPlanes collection object. |
| [Parent](../WorkPlanes/WorkPlanes_Parent.md) | Property returning the parent  object. |
| [Type](../WorkPlanes/WorkPlanes_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyComponentDefinition.WorkPlanes](../AssemblyComponentDefinition/AssemblyComponentDefinition_WorkPlanes.md), [FlatPattern.WorkPlanes](../FlatPattern/FlatPattern_WorkPlanes.md), [PartComponentDefinition.WorkPlanes](../PartComponentDefinition/PartComponentDefinition_WorkPlanes.md), [SheetMetalComponentDefinition.WorkPlanes](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_WorkPlanes.md), [WeldmentComponentDefinition.WorkPlanes](../WeldmentComponentDefinition/WeldmentComponentDefinition_WorkPlanes.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Create sheet metal lofted flange feature](../../sample-programs/LoftedFlangeFeatures_Add_Sample.md) | The following sample demonstrates the creation of a sheet metal lofted flange feature. |
| [Projection - project across parts](../../sample-programs/Sketch_AddByProjectingEntity_Sample.md) | This sample demonstrates projecting a sketch entity across parts in an assembly. To use the sample, have an assembly open that contains at least two occurrences, (parts only), and run the program. |
| [Spline - create NURBS](../../sample-programs/SketchFixedSpline_Sample.md) | This sample demonstrates the creation of a sketch spline using a geometry definition (a NURB). The API also supports creation of 3D sketch splines in a similar way. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |

## Version

Introduced in version 4
