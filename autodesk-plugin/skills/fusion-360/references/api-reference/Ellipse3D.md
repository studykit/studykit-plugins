# Ellipse3D Object

Derived from: [Curve3D](Curve3D.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/Ellipse3D.h>

## Description

Transient 3D ellipse. A transient ellipse is n0t displayed or saved in a document. Transient 3D ellipses are used as a wrapper to work with raw 3D ellipse information. They are created statically using the create method of the Ellipse3D class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Ellipse3D_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](Ellipse3D_copy.htm) | Creates a copy of this Ellipse3D object. |
| [create](Ellipse3D_create.htm) | Creates a transient 3D ellipse object. |
| [getData](Ellipse3D_getData.htm) | Gets all of the data defining the ellipse. |
| [set](Ellipse3D_set.htm) | Sets all of the data defining the ellipse. |
| [transformBy](Ellipse3D_transformBy.htm) | Transforms this curve in 3D space. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [asNurbsCurve](Ellipse3D_asNurbsCurve.htm) | Returns a NURBS curve that is geometrically identical to the ellipse. |
| [center](Ellipse3D_center.htm) | Gets and sets the center position of the ellipse. |
| [curveType](Ellipse3D_curveType.htm) | Returns the type of geometry this curve represents. |
| [evaluator](Ellipse3D_evaluator.htm) | Returns an evaluator object that lets you perform additional evaluations on the curve. |
| [isValid](Ellipse3D_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [majorAxis](Ellipse3D_majorAxis.htm) | Gets and sets the major axis of the ellipse. |
| [majorRadius](Ellipse3D_majorRadius.htm) | Gets and sets the major radius of the ellipse. |
| [minorRadius](Ellipse3D_minorRadius.htm) | Gets and sets the minor radius of the ellipse. |
| [normal](Ellipse3D_normal.htm) | Gets the normal of the ellipse. |
| [objectType](Ellipse3D_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Ellipse3D.copy](Ellipse3D_copy.htm), [Ellipse3D.create](Ellipse3D_create.htm), [SketchEllipse.geometry](SketchEllipse_geometry.htm), [SketchEllipse.worldGeometry](SketchEllipse_worldGeometry.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |