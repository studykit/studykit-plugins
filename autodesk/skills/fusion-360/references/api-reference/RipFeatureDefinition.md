# RipFeatureDefinition Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeatureDefinition.h>

## Description

A Base class to return the information used to define the RipFeature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](RipFeatureDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](RipFeatureDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](RipFeatureDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[RipFeature.definition](RipFeature_definition.htm)

## Derived Classes

[AlongEdgeRipFeatureDefinition](AlongEdgeRipFeatureDefinition.htm), [BetweenPointsRipFeatureDefinition](BetweenPointsRipFeatureDefinition.htm), [FaceRipFeatureDefinition](FaceRipFeatureDefinition.htm)

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