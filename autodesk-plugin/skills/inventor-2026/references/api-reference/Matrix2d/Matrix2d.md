# Matrix2d Object

## Description

A 3x3 Matrix2d object. For more information, see the Transient Geometry article on the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../Matrix2d/Matrix2d_Copy.md) | Creates a copy of this Matrix2d object. The result is entirely independent and can be edited without affecting the original Matrix2d object. |
| [GetCoordinateSystem](../Matrix2d/Matrix2d_GetCoordinateSystem.md) | Get the coordinate system that this matrix2d maps to from the standard coordinate system. |
| [GetMatrixData](../Matrix2d/Matrix2d_GetMatrixData.md) | Get the data defining this matrix. |
| [Invert](../Matrix2d/Matrix2d_Invert.md) | Method to Invert this matrix2d. |
| [IsEqualTo](../Matrix2d/Matrix2d_IsEqualTo.md) | Compares this matrix2d for equality with the specified matrix2d |
| [PostMultiplyBy](../Matrix2d/Matrix2d_PostMultiplyBy.md) | Post multiply this matrix2d by the specified matrix2d, setting this matrix2d to the result. |
| [PreMultiplyBy](../Matrix2d/Matrix2d_PreMultiplyBy.md) | Pre multiply this matrix2d by the specified matrix2d, setting this matrix2d to the result. |
| [PutMatrixData](../Matrix2d/Matrix2d_PutMatrixData.md) | Method that sets the data defining this matrix. |
| [SetCoordinateSystem](../Matrix2d/Matrix2d_SetCoordinateSystem.md) | Sets this matrix2d to be the matrix2d that maps from the standard coordinate system to the specified coordinate system. |
| [SetToAlignCoordinateSystems](../Matrix2d/Matrix2d_SetToAlignCoordinateSystems.md) | Sets this matrix2d to be the matrix2d that maps from the 'from' coordinate system to the 'to' coordinate system. |
| [SetToIdentity](../Matrix2d/Matrix2d_SetToIdentity.md) | Sets this matrix2d to the identity matrix2d. |
| [SetToRotateTo](../Matrix2d/Matrix2d_SetToRotateTo.md) | Sets to the matrix2d of rotation that would align the 'from' vector2d with the 'to' vector2d. |
| [SetToRotation](../Matrix2d/Matrix2d_SetToRotation.md) | Sets this matrix2d to the matrix2d of rotation by the specified angle, through the specified origin. |
| [SetTranslation](../Matrix2d/Matrix2d_SetTranslation.md) | Sets the translation portion of the matrix2d. |
| [TransformBy](../Matrix2d/Matrix2d_TransformBy.md) | Set this matrix2d to the result of this transformation followed by the specified transformation (a pre multiplication of this matrix2d by the specified matrix2d). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Cell](../Matrix2d/Matrix2d_Cell.md) | Property that returns the cell defined by row/col. |
| [Determinant](../Matrix2d/Matrix2d_Determinant.md) | Get the determinant of this matrix2d. |
| [Translation](../Matrix2d/Matrix2d_Translation.md) | Get the translation portion of the matrix2d. |

## Accessed From

[AutoCADBlock.Transformation](../AutoCADBlock/AutoCADBlock_Transformation.md), [Matrix2d.Copy](../Matrix2d/Matrix2d_Copy.md), [SketchBlock.Transformation](../SketchBlock/SketchBlock_Transformation.md), [SketchBlockProxy.Transformation](../SketchBlockProxy/SketchBlockProxy_Transformation.md), [SketchedSymbol.Transformation](../SketchedSymbol/SketchedSymbol_Transformation.md), [TitleBlock.Transformation](../TitleBlock/TitleBlock_Transformation.md), [TransientGeometry.CreateMatrix2d](../TransientGeometry/TransientGeometry_CreateMatrix2d.md)

## Version

Introduced in version 4
