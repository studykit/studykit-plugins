# SketchCurves Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCurves.h>

## Description

A collection of sketch curves in a sketch. This also provides access to collections for the specific types of curves where you can get the curves based on type and create new curves.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](SketchCurves_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](SketchCurves_item.htm) | Function that returns the specified sketch curve using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](SketchCurves_count.htm) | Returns the number of sketch curves in the sketch. |
| [isValid](SketchCurves_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](SketchCurves_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [sketchArcs](SketchCurves_sketchArcs.htm) | Returns the sketch arcs collection associated with this sketch. This provides access to the existing sketch arcs and supports the creation of new sketch arcs. |
| [sketchCircles](SketchCurves_sketchCircles.htm) | Returns the sketch circles collection associated with this sketch. This provides access to the existing sketch circles and supports the creation of new sketch circles. |
| [sketchConicCurves](SketchCurves_sketchConicCurves.htm) | Returns the conic curves collection associated with this sketch. This provides access to the existing conic curves and supports the creation of new conic curves. |
| [sketchControlPointSplines](SketchCurves_sketchControlPointSplines.htm) | Returns the control point splines collection associated with this sketch. This provides access to the existing control point splines and supports the creation of new control point splines. |
| [sketchEllipses](SketchCurves_sketchEllipses.htm) | Returns the sketch ellipses collection associated with this sketch. This provides access to the existing sketch ellipses and supports the creation of new sketch ellipses. |
| [sketchEllipticalArcs](SketchCurves_sketchEllipticalArcs.htm) | Returns the sketch elliptical arcs collection associated with this sketch. This provides access to the existing sketch elliptical arcs and supports the creation of new sketch elliptical arcs. |
| [sketchFittedSplines](SketchCurves_sketchFittedSplines.htm) | Returns the sketch splines collection associated with this sketch. This provides access to the existing sketch splines and supports the creation of new sketch splines. |
| [sketchFixedSplines](SketchCurves_sketchFixedSplines.htm) | Returns the fixed sketch splines collection associated with this sketch. This provides access to the existing fixed sketch splines and supports the creation of new fixed sketch splines. |
| [sketchLines](SketchCurves_sketchLines.htm) | Returns the sketch lines collection associated with this sketch. This provides access to the existing sketch lines and supports the creation of new sketch lines. |

## Accessed From

[Sketch.sketchCurves](Sketch_sketchCurves.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [API Sample that demonstrates creating sketch lines in various ways.](CreateSketchLines_Sample.htm) | Demonstrates several ways to create sketch lines, including as the result of creating a rectangle. |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |
| [Simple Extrusion Sample](SimpleExtrusionSample_Sample.htm) | Creates a new extrusion feature, resulting in a new component. |
| [Simple Revolve Feature Sample](SimpleRevolveFeatureSample_Sample.htm) | Creates a new revolve feature, resulting in a new component. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |