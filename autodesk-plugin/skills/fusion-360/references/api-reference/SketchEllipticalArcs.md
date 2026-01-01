# SketchEllipticalArcs Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipticalArcs.h>

## Description

The collection of elliptical arcs in a sketch. This provides access to the existing elliptical arcs and supports the methods to create new elliptical arcs.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addByAngle](SketchEllipticalArcs_addByAngle.htm) | Creates an elliptical sketch arc where the sweep of the arc is defined by the start and sweep angles. |
| [addByEndPoints](SketchEllipticalArcs_addByEndPoints.htm) | Creates an elliptical sketch arc where the sweep of the arc is defined by two points. |
| [classType](SketchEllipticalArcs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](SketchEllipticalArcs_item.htm) | Function that returns the specified sketch elliptical arc using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](SketchEllipticalArcs_count.htm) | Returns the number of elliptical arcs in the sketch. |
| [isValid](SketchEllipticalArcs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](SketchEllipticalArcs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[SketchCurves.sketchEllipticalArcs](SketchCurves_sketchEllipticalArcs.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |