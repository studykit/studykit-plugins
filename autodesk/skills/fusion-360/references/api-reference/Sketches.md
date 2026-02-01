# Sketches Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketches.h>

## Description

Provides access to the sketches within a design and provides methods to create new sketches.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](Sketches_add.htm) | Creates a new sketch on the specified planar entity. |
| [addToBaseOrFormFeature](Sketches_addToBaseOrFormFeature.htm) | Creates a parametric sketch that is associated with a base feature. |
| [addWithoutEdges](Sketches_addWithoutEdges.htm) | Creates a new sketch on the specified planar entity. If a BRepFace is provided, the edges of the face are not projected into the sketch so the result of creating a new sketch with this method will always be a new empty sketch. |
| [classType](Sketches_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](Sketches_item.htm) | Function that returns the specified sketch using an index into the collection. |
| [itemByName](Sketches_itemByName.htm) | Returns the sketch with the specified name. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](Sketches_count.htm) | Returns the number of sketches in a component |
| [isValid](Sketches_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Sketches_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[Component.sketches](Component_sketches.htm), [FlatPatternComponent.sketches](FlatPatternComponent_sketches.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [API Sample that demonstrates creating sketch lines in various ways.](CreateSketchLines_Sample.htm) | Demonstrates several ways to create sketch lines, including as the result of creating a rectangle. |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |