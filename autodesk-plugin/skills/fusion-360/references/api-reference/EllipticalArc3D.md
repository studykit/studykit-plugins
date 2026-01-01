# EllipticalArc3D Object

Derived from: [Curve3D](Curve3D.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalArc3D.h>

## Description

Transient 3D elliptical arc. A transient elliptical arc is not displayed or saved in a document. Transient 3D elliptical arcs are used as a wrapper to work with raw 3D elliptical arc information. They are created statically using the create method of the EllipticalArc3D class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](EllipticalArc3D_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](EllipticalArc3D_copy.htm) | Creates and returns a copy of this EllipticalArc3D object. |
| [create](EllipticalArc3D_create.htm) | Creates a transient 3D elliptical arc. |
| [getData](EllipticalArc3D_getData.htm) | Gets all of the data defining the elliptical arc. |
| [set](EllipticalArc3D_set.htm) | Sets all of the data defining the elliptical arc. |
| [transformBy](EllipticalArc3D_transformBy.htm) | Transforms this curve in 3D space. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [asNurbsCurve](EllipticalArc3D_asNurbsCurve.htm) | Returns a NURBS curve that is geometrically identical to the elliptical arc. |
| [center](EllipticalArc3D_center.htm) | Gets and sets the center point of the elliptical arc. |
| [curveType](EllipticalArc3D_curveType.htm) | Returns the type of geometry this curve represents. |
| [endAngle](EllipticalArc3D_endAngle.htm) | Gets and sets the end angle of the elliptical arc. |
| [evaluator](EllipticalArc3D_evaluator.htm) | Returns an evaluator object that lets you perform additional evaluations on the curve. |
| [isValid](EllipticalArc3D_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [majorAxis](EllipticalArc3D_majorAxis.htm) | Gets and sets the major axis of the elliptical arc. |
| [majorRadius](EllipticalArc3D_majorRadius.htm) | Gets and sets the major radius of the elliptical arc. |
| [minorRadius](EllipticalArc3D_minorRadius.htm) | Gets and sets the minor radius of the elliptical arc. |
| [normal](EllipticalArc3D_normal.htm) | Gets the normal of the elliptical arc. |
| [objectType](EllipticalArc3D_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [startAngle](EllipticalArc3D_startAngle.htm) | Gets and sets the start angle of the elliptical arc. |

## Accessed From

[EllipticalArc3D.copy](EllipticalArc3D_copy.htm), [EllipticalArc3D.create](EllipticalArc3D_create.htm), [SketchEllipticalArc.geometry](SketchEllipticalArc_geometry.htm), [SketchEllipticalArc.worldGeometry](SketchEllipticalArc_worldGeometry.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |