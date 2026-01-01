# Curve3D Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/Curve3D.h>

## Description

The base class for all 3D transient geometry classes.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Curve3D_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [transformBy](Curve3D_transformBy.htm) | Transforms this curve in 3D space. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [curveType](Curve3D_curveType.htm) | Returns the type of geometry this curve represents. |
| [evaluator](Curve3D_evaluator.htm) | Returns an evaluator object that lets you perform additional evaluations on the curve. |
| [isValid](Curve3D_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Curve3D_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[BRepEdge.geometry](BRepEdge_geometry.htm), [BRepEdgeDefinition.modelSpaceCurve](BRepEdgeDefinition_modelSpaceCurve.htm), [BRepWireEdgeDefinition.modelSpaceCurve](BRepWireEdgeDefinition_modelSpaceCurve.htm), [Curve3DPath.item](Curve3DPath_item.htm), [CustomGraphicsCurve.curve](CustomGraphicsCurve_curve.htm), [PathEntity.curve](PathEntity_curve.htm), [ProfileCurve.geometry](ProfileCurve_geometry.htm), [SketchText.asCurves](SketchText_asCurves.htm)

## Derived Classes

[Arc3D](Arc3D.htm), [Circle3D](Circle3D.htm), [Ellipse3D](Ellipse3D.htm), [EllipticalArc3D](EllipticalArc3D.htm), [InfiniteLine3D](InfiniteLine3D.htm), [Line3D](Line3D.htm), [NurbsCurve3D](NurbsCurve3D.htm), [Polyline3D](Polyline3D.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |