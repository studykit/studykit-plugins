# RipFeatureInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeatureInput.h>

## Description

This class defines the methods and properties that pertain to the definition of a Rip feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](RipFeatureInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [setAlongEdge](RipFeatureInput_setAlongEdge.htm) | Specifies the rip feature will be along an edge. |
| [setBetweenPoints](RipFeatureInput_setBetweenPoints.htm) | This input method is for creating a rip between two points. Each point can be either a BRepVertex or a BRepEdge and an associated offset along the edge. |
| [setByFace](RipFeatureInput_setByFace.htm) | Specifies the rip feature will be defined by a face.. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](RipFeatureInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](RipFeatureInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[RipFeatures.createRipFeatureInput](RipFeatures_createRipFeatureInput.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Rip Feature Sample](RipFeatureSample_Sample.htm) | Demonstrates creating a new sheet metal rip feature. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |