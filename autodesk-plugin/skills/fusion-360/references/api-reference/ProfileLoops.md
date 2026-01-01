# ProfileLoops Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ProfileLoops.h>

## Description

A collection of loops within a Profile.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ProfileLoops_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](ProfileLoops_item.htm) | Function that returns the specified profile loop using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ProfileLoops_count.htm) | Returns the number of loops within this profile. |
| [isValid](ProfileLoops_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ProfileLoops_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Profile.profileLoops](Profile_profileLoops.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |