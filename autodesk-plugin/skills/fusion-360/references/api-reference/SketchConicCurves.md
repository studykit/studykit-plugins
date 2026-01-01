# SketchConicCurves Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchConicCurves.h>

## Description

The collection of conic curves in a sketch. This provides access to the existing conic curves and supports the method to create new conic curves.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](SketchConicCurves_add.htm) | Creates a new conic curve. |
| [classType](SketchConicCurves_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](SketchConicCurves_item.htm) | Function that returns the specified conic curve using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](SketchConicCurves_count.htm) | Returns the number of conic curves in the sketch. |
| [isValid](SketchConicCurves_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](SketchConicCurves_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[SketchCurves.sketchConicCurves](SketchCurves_sketchConicCurves.htm)

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |