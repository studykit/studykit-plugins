# Vector2d Object

## Description

The Vector2d object. For more information, see the [Transient Geometry](TransientGeometry_Overview.md) overview.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddVector](../Vector2d/Vector2d_AddVector.md) | Add the specified vector2d to this vector2d. |
| [AngleTo](../Vector2d/Vector2d_AngleTo.md) | Determines the angle between this vector2d and the specified vector2d. |
| [AsUnitVector](../Vector2d/Vector2d_AsUnitVector.md) | Get the unit vector2d equivalent of this vector2d normalized. |
| [Copy](../Vector2d/Vector2d_Copy.md) | Creates a copy of this Vector2d object. The result is entirely independent and can be edited without affecting the original Vector2d object. |
| [DotProduct](../Vector2d/Vector2d_DotProduct.md) | Determine the dot product of this vector2d to the specified vector2d. |
| [GetVectorData](../Vector2d/Vector2d_GetVectorData.md) | Get the data defining this vector. |
| [IsEqualTo](../Vector2d/Vector2d_IsEqualTo.md) | Compare this vector2d for equality to the specified vector2d. |
| [IsParallelTo](../Vector2d/Vector2d_IsParallelTo.md) | Determine if this vector2d is parallel to the specified vector2d. |
| [IsPerpendicularTo](../Vector2d/Vector2d_IsPerpendicularTo.md) | Determine if this vector2d is perpendicular to the specified vector2d. |
| [Normalize](../Vector2d/Vector2d_Normalize.md) | Normalize this vector2d to result in a length equal to 1.0. |
| [PutVectorData](../Vector2d/Vector2d_PutVectorData.md) | Method that sets the data defining this vector. |
| [ScaleBy](../Vector2d/Vector2d_ScaleBy.md) | Scale this vector2d by the specified scale factor. |
| [SubtractVector](../Vector2d/Vector2d_SubtractVector.md) | Subtract the specified vector2d from this vector2d. |
| [TransformBy](../Vector2d/Vector2d_TransformBy.md) | Transform this vector2d by the specified matrix. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Length](../Vector2d/Vector2d_Length.md) | Get the length of this vector2d. |
| [X](../Vector2d/Vector2d_X.md) | Gets the X-component for this Vector2d. |
| [Y](../Vector2d/Vector2d_Y.md) | Gets the Y-component for this Vector2d. |

## Accessed From

[EllipseFull2d.MajorAxisVector](../EllipseFull2d/EllipseFull2d_MajorAxisVector.md), [Matrix2d.GetCoordinateSystem](../Matrix2d/Matrix2d_GetCoordinateSystem.md), [Matrix2d.Translation](../Matrix2d/Matrix2d_Translation.md), [Point2d.VectorTo](../Point2d/Point2d_VectorTo.md), [TransientGeometry.CreateVector2d](../TransientGeometry/TransientGeometry_CreateVector2d.md), [UnitVector2d.AsVector](../UnitVector2d/UnitVector2d_AsVector.md), [Vector2d.Copy](../Vector2d/Vector2d_Copy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Move sketch entities](../../sample-programs/Sketch_MoveSketchObjects_Sample.md) | This sample demonstrates the translation of all the objects on the active sketch by a certain distance. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |