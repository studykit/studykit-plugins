# Curve2D Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/Curve2D.h>

## Description

The base class for all 2D transient geometry classes.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Curve2D_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [transformBy](Curve2D_transformBy.htm) | Transforms this curve in 2D space. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [curveType](Curve2D_curveType.htm) | Returns the type of geometry this curve represents. |
| [evaluator](Curve2D_evaluator.htm) | Returns an evaluator object that lets you perform additional evaluations on the curve. |
| [isValid](Curve2D_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Curve2D_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[BRepCoEdge.geometry](BRepCoEdge_geometry.htm)

## Derived Classes

[Arc2D](Arc2D.htm), [Circle2D](Circle2D.htm), [Ellipse2D](Ellipse2D.htm), [EllipticalArc2D](EllipticalArc2D.htm), [Line2D](Line2D.htm), [NurbsCurve2D](NurbsCurve2D.htm), [Polyline2D](Polyline2D.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |