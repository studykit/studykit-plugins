# EllipticalCylinder Object

Derived from: [Surface](Surface.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalCylinder.h>

## Description

Transient elliptical cylinder. A transient elliptical cylinder is not displayed or saved in a document. A transient elliptical cylinder is used as a wrapper to work with raw elliptical cylinder information. A transient elliptical cylinder has no boundaries and is infinite in length. They are created statically using the create method of the EllipticalCylinder class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](EllipticalCylinder_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](EllipticalCylinder_copy.htm) | Creates and returns an independent copy of this EllipticalCylinder object. |
| [create](EllipticalCylinder_create.htm) | Creates a transient 3D elliptical cylinder object. |
| [getData](EllipticalCylinder_getData.htm) | Gets the data defining the elliptical cylinder. |
| [set](EllipticalCylinder_set.htm) | Sets the data defining the elliptical cylinder. |
| [transformBy](EllipticalCylinder_transformBy.htm) | Updates this surface by transforming it with a given input matrix. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [axis](EllipticalCylinder_axis.htm) | Gets and set the center axis (along the length) of the cylinder that defines its normal direction. |
| [evaluator](EllipticalCylinder_evaluator.htm) | Returns the surface evaluator. |
| [isValid](EllipticalCylinder_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [majorAxis](EllipticalCylinder_majorAxis.htm) | Gets and sets the direction of the major axis of the ellipse that defines the cylinder. |
| [majorRadius](EllipticalCylinder_majorRadius.htm) | Gets and sets the major radius of the ellipse that defines the cylinder. |
| [minorRadius](EllipticalCylinder_minorRadius.htm) | Gets and sets the minor radius of the ellipse that defines the cylinder. |
| [objectType](EllipticalCylinder_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [origin](EllipticalCylinder_origin.htm) | Gets and sets the origin point (center) of the base of the cylinder. |
| [surfaceType](EllipticalCylinder_surfaceType.htm) | Returns the surface type. |

## Accessed From

[EllipticalCylinder.copy](EllipticalCylinder_copy.htm), [EllipticalCylinder.create](EllipticalCylinder_create.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |