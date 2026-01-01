# BRepLoops Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLoops.h>

## Description

BRepLoop collection.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BRepLoops_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](BRepLoops_item.htm) | Function that returns the specified loop using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](BRepLoops_count.htm) | The number of loops in the collection. |
| [isValid](BRepLoops_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BRepLoops_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[BRepFace.loops](BRepFace_loops.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |