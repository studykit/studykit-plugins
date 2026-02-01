# Sphere Object

Derived from: [Surface](Surface.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/Sphere.h>

## Description

Transient sphere. A transient sphere is not displayed or saved in a document. Transient spheres are used as a wrapper to work with raw sphere information. A transient sphere is a full sphere defined by a point and a radius. They are created statically using the create method of the Sphere class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Sphere_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](Sphere_copy.htm) | Creates and returns an independent copy of this Sphere object. |
| [create](Sphere_create.htm) | Creates a transient sphere object. |
| [getData](Sphere_getData.htm) | Gets all of the data defining the sphere. |
| [set](Sphere_set.htm) | Sets all of the data defining the sphere. |
| [transformBy](Sphere_transformBy.htm) | Updates this surface by transforming it with a given input matrix. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [evaluator](Sphere_evaluator.htm) | Returns the surface evaluator. |
| [isValid](Sphere_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Sphere_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [origin](Sphere_origin.htm) | Gets and sets the origin point (center) of the sphere. |
| [radius](Sphere_radius.htm) | Gets and sets the radius of the sphere. |
| [surfaceType](Sphere_surfaceType.htm) | Returns the surface type. |

## Accessed From

[Sphere.copy](Sphere_copy.htm), [Sphere.create](Sphere_create.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |