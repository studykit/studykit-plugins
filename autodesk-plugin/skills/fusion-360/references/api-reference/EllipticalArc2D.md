# EllipticalArc2D Object

Derived from: [Curve2D](Curve2D.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalArc2D.h>

## Description

Transient 2D elliptical arc. A transient elliptical arc is not displayed or saved in a document. Transient 2D elliptical arcs are used as a wrapper to work with raw 2D elliptical arc information. They are created statically using the create method of the EllipticalArc2D class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](EllipticalArc2D_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](EllipticalArc2D_copy.htm) | Creates and returns a copy of this EllipticalArc2D object. |
| [create](EllipticalArc2D_create.htm) | Creates a transient 2D elliptical arc |
| [getData](EllipticalArc2D_getData.htm) | Gets all of the data defining the elliptical arc. |
| [set](EllipticalArc2D_set.htm) | Sets all of the data defining the elliptical arc. |
| [transformBy](EllipticalArc2D_transformBy.htm) | Transforms this curve in 2D space. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [asNurbsCurve](EllipticalArc2D_asNurbsCurve.htm) | Returns a NURBS curve that is geometrically identical to the elliptical arc. |
| [center](EllipticalArc2D_center.htm) | Gets and sets the center position of the elliptical arc. |
| [curveType](EllipticalArc2D_curveType.htm) | Returns the type of geometry this curve represents. |
| [endAngle](EllipticalArc2D_endAngle.htm) | Gets and sets the end angle of the elliptical arc in radians, where 0 is along the major axis. |
| [endPoint](EllipticalArc2D_endPoint.htm) | Gets the position of the end point of the elliptical arc. |
| [evaluator](EllipticalArc2D_evaluator.htm) | Returns an evaluator object that lets you perform additional evaluations on the curve. |
| [isCircular](EllipticalArc2D_isCircular.htm) | Gets if the elliptical arc is the geometric equivalent of a circular arc |
| [isClockwise](EllipticalArc2D_isClockwise.htm) | Gets if the sweep direction of the elliptical arc is clockwise or counterclockwise. |
| [isValid](EllipticalArc2D_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [majorAxis](EllipticalArc2D_majorAxis.htm) | Gets and sets the major axis of the elliptical arc. |
| [majorRadius](EllipticalArc2D_majorRadius.htm) | Gets and sets the major radius of the elliptical arc. |
| [minorRadius](EllipticalArc2D_minorRadius.htm) | Gets and sets the minor radius of the elliptical arc. |
| [objectType](EllipticalArc2D_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [startAngle](EllipticalArc2D_startAngle.htm) | Gets and sets the start angle of the elliptical arc in radians, where 0 is along the major axis. |
| [startPoint](EllipticalArc2D_startPoint.htm) | Gets the position of the start point of the elliptical arc. |

## Accessed From

[EllipticalArc2D.copy](EllipticalArc2D_copy.htm), [EllipticalArc2D.create](EllipticalArc2D_create.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |