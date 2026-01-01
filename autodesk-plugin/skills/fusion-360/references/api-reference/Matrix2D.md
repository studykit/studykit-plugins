# Matrix2D Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/Matrix2D.h>

## Description

Transient 2D 3x3 matrix. This object is a wrapper over 2D matrix data and is used as way to pass matrix data in and out of the API and as a convenience when operating on matrix data. They are created statically using the create method of the Matrix2D class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [asArray](Matrix2D_asArray.htm) | Returns the contents of the matrix as a 9 element array. |
| [classType](Matrix2D_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](Matrix2D_copy.htm) | Creates an independent copy of this matrix. |
| [create](Matrix2D_create.htm) | Creates a transient 2D matrix (3x3) object. It is initialized as an identity matrix. |
| [getAsCoordinateSystem](Matrix2D_getAsCoordinateSystem.htm) | Gets the matrix data as the components that define a coordinate system. |
| [getCell](Matrix2D_getCell.htm) | Gets the value of the specified cell in the 3x3 matrix. |
| [invert](Matrix2D_invert.htm) | Invert this matrix. |
| [isEqualTo](Matrix2D_isEqualTo.htm) | Compares this matrix with another matrix and returns True if they're identical. |
| [setCell](Matrix2D_setCell.htm) | Sets the specified cell in the 3x3 matrix to the specified value. |
| [setToAlignCoordinateSystems](Matrix2D_setToAlignCoordinateSystems.htm) | Sets this matrix to be the matrix that maps from the 'from' coordinate system to the 'to' coordinate system. |
| [setToIdentity](Matrix2D_setToIdentity.htm) | Resets this matrix to be an identity matrix. |
| [setToRotateTo](Matrix2D_setToRotateTo.htm) | Sets to the matrix of rotation that would align the 'from' vector with the 'to' vector. |
| [setToRotation](Matrix2D_setToRotation.htm) | Sets this matrix to the matrix of rotation by the specified angle, through the specified origin. |
| [setWithArray](Matrix2D_setWithArray.htm) | Sets the contents of the array using a 9 element array. |
| [setWithCoordinateSystem](Matrix2D_setWithCoordinateSystem.htm) | Reset this matrix to align with a specific coordinate system. |
| [transformBy](Matrix2D_transformBy.htm) | Transforms this matrix using the input matrix. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [determinant](Matrix2D_determinant.htm) | Returns the determinant of the matrix. |
| [isValid](Matrix2D_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Matrix2D_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Canvas.transform](Canvas_transform.htm), [CanvasInput.transform](CanvasInput_transform.htm), [Matrix2D.copy](Matrix2D_copy.htm), [Matrix2D.create](Matrix2D_create.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |