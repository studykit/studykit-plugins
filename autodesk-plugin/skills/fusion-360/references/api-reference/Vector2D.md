# Vector2D Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/Vector2D.h>

## Description

Transient 2D vector. This object is a wrapper for 2D vector data and is used to pass vector data in and out of the API. They are created statically using the create method of the Vector2D class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](Vector2D_add.htm) | Add a vector to this vector. |
| [angleTo](Vector2D_angleTo.htm) | Gets the angle between this vector and another vector. |
| [asArray](Vector2D_asArray.htm) | Returns the vector values as an array [x, y]. |
| [asPoint](Vector2D_asPoint.htm) | Return a point with the same x and y values as this vector. |
| [classType](Vector2D_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](Vector2D_copy.htm) | Creates and returns an independent copy of this Vector2D object. |
| [create](Vector2D_create.htm) | Creates a 2D vector object. |
| [dotProduct](Vector2D_dotProduct.htm) | Calculates the Dot Product of this vector and an input vector. |
| [isEqualTo](Vector2D_isEqualTo.htm) | Compare this vector with another to check for equality. |
| [isParallelTo](Vector2D_isParallelTo.htm) | Compare this vector with another to check for parallelism. |
| [isPerpendicularTo](Vector2D_isPerpendicularTo.htm) | Compare this vector with another to check for perpendicularity. |
| [normalize](Vector2D_normalize.htm) | Normalizes the vector. Normalization makes the vector length equal to one. The vector should not be zero length. |
| [scaleBy](Vector2D_scaleBy.htm) | Scales the vector by specifying a scaling factor. |
| [setWithArray](Vector2D_setWithArray.htm) | Sets the definition of the vector by specifying an array containing the x and y coordinates. |
| [subtract](Vector2D_subtract.htm) | Subtract a vector from this vector. |
| [transformBy](Vector2D_transformBy.htm) | Transforms the vector by specifying a 2D transformation matrix. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](Vector2D_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [length](Vector2D_length.htm) | Gets the length of the vector. |
| [objectType](Vector2D_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [x](Vector2D_x.htm) | Gets and sets the X coordinate of the vector. |
| [y](Vector2D_y.htm) | Gets and sets the Y coordinate of the vector. |

## Accessed From

[CurveEvaluator2D.getCurvature](CurveEvaluator2D_getCurvature.htm), [CurveEvaluator2D.getFirstDerivative](CurveEvaluator2D_getFirstDerivative.htm), [CurveEvaluator2D.getSecondDerivative](CurveEvaluator2D_getSecondDerivative.htm), [CurveEvaluator2D.getTangent](CurveEvaluator2D_getTangent.htm), [CurveEvaluator2D.getThirdDerivative](CurveEvaluator2D_getThirdDerivative.htm), [Ellipse2D.getData](Ellipse2D_getData.htm), [Ellipse2D.majorAxis](Ellipse2D_majorAxis.htm), [EllipticalArc2D.getData](EllipticalArc2D_getData.htm), [EllipticalArc2D.majorAxis](EllipticalArc2D_majorAxis.htm), [Matrix2D.getAsCoordinateSystem](Matrix2D_getAsCoordinateSystem.htm), [Point2D.asVector](Point2D_asVector.htm), [Point2D.vectorTo](Point2D_vectorTo.htm), [Vector2D.copy](Vector2D_copy.htm), [Vector2D.create](Vector2D_create.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |