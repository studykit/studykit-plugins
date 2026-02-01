# SketchFittedSplines Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFittedSplines.h>

## Description

The collection of fitted splines in a sketch. This provides access to the existing fitted splines and supports the methods to create new fitted splines.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](SketchFittedSplines_add.htm) | Creates a new fitted spline through the specified points. |
| [addByNurbsCurve](SketchFittedSplines_addByNurbsCurve.htm) | \*\*RETIRED\*\* Creates a new fitted spline using the input NurbsCurve3D to define the shape. Fit points are created to create a curve that exactly matches the input curve. |
| [classType](SketchFittedSplines_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](SketchFittedSplines_item.htm) | Function that returns the specified sketch fitted spline using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](SketchFittedSplines_count.htm) | Returns the number of fitted splines in the sketch. |
| [isValid](SketchFittedSplines_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](SketchFittedSplines_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[SketchCurves.sketchFittedSplines](SketchCurves_sketchFittedSplines.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchFittedSplines.add](SketchFittedSplines_add_Sample.htm) | Demonstrates the SketchFittedSplines.add method. |
| [Sketch spline through points creation and relative functions API Sample](SketchSplineThroughPoints_Sample.htm) | Create a sketch spline with points and use some operations for spline tangent handle & curvature handle. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |