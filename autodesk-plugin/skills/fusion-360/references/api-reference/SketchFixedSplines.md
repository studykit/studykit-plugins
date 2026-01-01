# SketchFixedSplines Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFixedSplines.h>

## Description

The collection of fixed splines in a sketch. Fixed splines are splines that were created as the result of some operation (i.e. intersection) and is not directly editable.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addByNurbsCurve](SketchFixedSplines_addByNurbsCurve.htm) | Creates a new fixed spline using the input NurbsCurve3D to define the shape. The resulting curve is not editable by the user but can be updated via the API using the replaceGeometry method on the SketchFixedSpline object. |
| [classType](SketchFixedSplines_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](SketchFixedSplines_item.htm) | Function that returns the specified sketch fixed spline using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](SketchFixedSplines_count.htm) | Returns the number of fitted splines in the sketch. |
| [isValid](SketchFixedSplines_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](SketchFixedSplines_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[SketchCurves.sketchFixedSplines](SketchCurves_sketchFixedSplines.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchFixedSplines.addByNurbsCurve](SketchFixedSplines_addByNurbsCurve_Sample.htm) | Demonstrates the SketchFixedSplines.addByNurbsCurve method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |