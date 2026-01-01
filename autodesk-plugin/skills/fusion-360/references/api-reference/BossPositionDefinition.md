# BossPositionDefinition Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossPositionDefinition.h>

## Description

The base class for the classes that define how a boss feature can be positioned.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BossPositionDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](BossPositionDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BossPositionDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[BossFeature.positionDefinition](BossFeature_positionDefinition.htm)

## Derived Classes

[SketchPointsBossPositionDefinition](SketchPointsBossPositionDefinition.htm)

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |