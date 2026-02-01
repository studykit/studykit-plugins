# SketchPoints Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchPoints.h>

## Description

A collection of sketch points.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](SketchPoints_add.htm) | Creates a point at the specified location. This is the equivalent of creating a sketch point using the Point command in the user interface and will create a visible point in the graphics window. |
| [classType](SketchPoints_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](SketchPoints_item.htm) | Function that returns the specified sketch using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](SketchPoints_count.htm) | Returns the number of sketch points in the sketch. |
| [isValid](SketchPoints_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](SketchPoints_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Sketch.sketchPoints](Sketch_sketchPoints.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [GeometricConstraints.addCoincident](GeometricConstraints_addCoincident_Sample.htm) | Demonstrates the GeometricConstraints.addCoincident method. |
| [SketchPoint.add](SketchPoint_add_Sample.htm) | Demonstrates the SketchPoint.add method. |
| [Sketch Point API Sample](SketchPointSample_Sample.htm) | Demonstrates creating a new sketch point. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |