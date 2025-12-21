# Vector Object

## Description

The Vector object. For more information, see the [Transient Geometry](TransientGeometry_Overview.md) overview.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddVector](../Vector/Vector_AddVector.md) | Add the specified vector to this vector. |
| [AngleTo](../Vector/Vector_AngleTo.md) | Determines the angle between this vector and the specified vector. |
| [AsUnitVector](../Vector/Vector_AsUnitVector.md) | Get the unit vector equivalent of this vector normalized. |
| [Copy](../Vector/Vector_Copy.md) | Creates a copy of this Vector object. The result is entirely independent and can be edited without affecting the original Vector object. |
| [CrossProduct](../Vector/Vector_CrossProduct.md) | Determine the cross product between this vector and the specified vector. |
| [DotProduct](../Vector/Vector_DotProduct.md) | Determine the dot product of this vector to the specified vector. |
| [GetVectorData](../Vector/Vector_GetVectorData.md) | Get the data defining this vector. |
| [IsEqualTo](../Vector/Vector_IsEqualTo.md) | Compare this vector for equality to the specified vector. |
| [IsParallelTo](../Vector/Vector_IsParallelTo.md) | Determine if this vector is parallel to the specified vector. |
| [IsPerpendicularTo](../Vector/Vector_IsPerpendicularTo.md) | Determine if this vector is perpendicular to the specified vector. |
| [Normalize](../Vector/Vector_Normalize.md) | Normalize this vector to result in a length equal to 1.0. |
| [PutVectorData](../Vector/Vector_PutVectorData.md) | Method that sets the data defining this vector. |
| [ScaleBy](../Vector/Vector_ScaleBy.md) | Scale this vector by the specified scale factor. |
| [SubtractVector](../Vector/Vector_SubtractVector.md) | Subtract the specified vector from this vector. |
| [TransformBy](../Vector/Vector_TransformBy.md) | Transform this vector by the specified matrix. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Length](../Vector/Vector_Length.md) | Get the length of this vector. |
| [X](../Vector/Vector_X.md) | Specifies the X coordinate of the vector. If not supplied, the X value will default to 0. |
| [Y](../Vector/Vector_Y.md) | Specifies the Y coordinate of the vector. If not supplied, the Y value will default to 0. |
| [Z](../Vector/Vector_Z.md) | Specifies the Z coordinate of the vector. If not supplied, the Z value will default to 0. |

## Accessed From

[DerivedPartCoordinateSystemDef.GetCoordinateSystem](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_GetCoordinateSystem.md), [DSLoadDefinition.Vector](../DSLoadDefinition/DSLoadDefinition_Vector.md), [EllipseFull.MajorAxisVector](../EllipseFull/EllipseFull_MajorAxisVector.md), [EllipticalCone.MajorAxisVector](../EllipticalCone/EllipticalCone_MajorAxisVector.md), [EllipticalCylinder.MajorAxisVector](../EllipticalCylinder/EllipticalCylinder_MajorAxisVector.md), [HoleTapInfo.ThreadDirection](../HoleTapInfo/HoleTapInfo_ThreadDirection.md), [Light.Direction](../Light/Light_Direction.md), [Matrix.GetCoordinateSystem](../Matrix/Matrix_GetCoordinateSystem.md), [Matrix.Translation](../Matrix/Matrix_Translation.md), [OrientedBox.DirectionOne](../OrientedBox/OrientedBox_DirectionOne.md), [OrientedBox.DirectionThree](../OrientedBox/OrientedBox_DirectionThree.md), [OrientedBox.DirectionTwo](../OrientedBox/OrientedBox_DirectionTwo.md), [OrientedBox.GetOrientedBoxData](../OrientedBox/OrientedBox_GetOrientedBoxData.md), [Point.VectorTo](../Point/Point_VectorTo.md), [PresentationTweak.Translation](PresentationTweak_Translation.md), [RegionProperties.PrincipalAxes](../RegionProperties/RegionProperties_PrincipalAxes.md), [StandardThreadInfo.ThreadDirection](../StandardThreadInfo/StandardThreadInfo_ThreadDirection.md), [TaperedThreadInfo.ThreadDirection](../TaperedThreadInfo/TaperedThreadInfo_ThreadDirection.md), [ThreadInfo.ThreadDirection](../ThreadInfo/ThreadInfo_ThreadDirection.md), [TransientGeometry.CreateVector](../TransientGeometry/TransientGeometry_CreateVector.md), [UnitVector.AsVector](../UnitVector/UnitVector_AsVector.md), [Vector.Copy](../Vector/Vector_Copy.md), [Vector.CrossProduct](../Vector/Vector_CrossProduct.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |