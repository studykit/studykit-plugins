# AsBuiltJointList Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJointList.h>

## Description

A list of as-built joints.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](AsBuiltJointList_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](AsBuiltJointList_item.htm) | Function that returns the specified as-built joint using an index into the list. |
| [itemByName](AsBuiltJointList_itemByName.htm) | Function that returns the specified as-built joint using a name. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](AsBuiltJointList_count.htm) | Returns number of as-built joints in the list. |
| [isValid](AsBuiltJointList_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](AsBuiltJointList_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Occurrence.asBuiltJoints](Occurrence_asBuiltJoints.htm)

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |