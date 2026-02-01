# LoftEndCondition Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftEndCondition.h>

## Description

The base class for all loft end conditions.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](LoftEndCondition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](LoftEndCondition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](LoftEndCondition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentLoftSection](LoftEndCondition_parentLoftSection.htm) | Returns the parent loft section. |

## Accessed From

[LoftSection.endCondition](LoftSection_endCondition.htm)

## Derived Classes

[LoftDirectionEndCondition](LoftDirectionEndCondition.htm), [LoftFreeEndCondition](LoftFreeEndCondition.htm), [LoftPointSharpEndCondition](LoftPointSharpEndCondition.htm), [LoftPointTangentEndCondition](LoftPointTangentEndCondition.htm), [LoftSmoothEndCondition](LoftSmoothEndCondition.htm), [LoftTangentEndCondition](LoftTangentEndCondition.htm)

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |