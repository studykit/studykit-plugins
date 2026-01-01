# Cylinder Object

Derived from: [Surface](Surface.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/Cylinder.h>

## Description

Transient cylinder. A transient cylinder is not displayed or saved in a document. A transient cylinder is but is used as a wrapper to work with raw cylinder information. A transient cylinder has no boundaries and is infinite in length. They are created statically using the create method of the Cylinder class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Cylinder_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](Cylinder_copy.htm) | Creates and returns an independent copy of this Cylinder object. |
| [create](Cylinder_create.htm) | Creates a transient cylinder object. |
| [getData](Cylinder_getData.htm) | Gets the data that defines the cylinder. |
| [set](Cylinder_set.htm) | Sets the data that defines the cylinder. |
| [transformBy](Cylinder_transformBy.htm) | Updates this surface by transforming it with a given input matrix. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [axis](Cylinder_axis.htm) | The center axis (along the length) of the cylinder that defines its normal direction. |
| [evaluator](Cylinder_evaluator.htm) | Returns the surface evaluator. |
| [isValid](Cylinder_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Cylinder_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [origin](Cylinder_origin.htm) | The origin point (center) of the base of the cylinder. |
| [radius](Cylinder_radius.htm) | The radius of the cylinder. |
| [surfaceType](Cylinder_surfaceType.htm) | Returns the surface type. |

## Accessed From

[Cylinder.copy](Cylinder_copy.htm), [Cylinder.create](Cylinder_create.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |