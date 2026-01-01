# Torus Object

Derived from: [Surface](Surface.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/Torus.h>

## Description

Transient torus. A transient torus is not displayed or saved in a document. A transient torus is used as a wrapper to work with raw torus information. A transient torus is a full torus with no boundaries. They are created statically using the create method of the Torus class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Torus_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](Torus_copy.htm) | Creates and returns an independent copy of this Torus object. |
| [create](Torus_create.htm) | Creates a transient torus object. |
| [getData](Torus_getData.htm) | Gets all of the data defining the torus. |
| [set](Torus_set.htm) | Sets all of the data defining the torus. |
| [transformBy](Torus_transformBy.htm) | Updates this surface by transforming it with a given input matrix. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [axis](Torus_axis.htm) | Gets and sets the center axis of the torus. |
| [evaluator](Torus_evaluator.htm) | Returns the surface evaluator. |
| [isValid](Torus_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [majorRadius](Torus_majorRadius.htm) | Gets and sets the major radius of the torus. |
| [minorRadius](Torus_minorRadius.htm) | Gets and sets the minor radius of the torus. |
| [objectType](Torus_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [origin](Torus_origin.htm) | Gets and sets the origin point (center) of the torus. |
| [surfaceType](Torus_surfaceType.htm) | Returns the surface type. |

## Accessed From

[Torus.copy](Torus_copy.htm), [Torus.create](Torus_create.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |