# RigidGroupList Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RigidGroupList.h>

## Description

A list of rigid groups.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](RigidGroupList_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](RigidGroupList_item.htm) | Function that returns the specified rigid group using an index into the list. |
| [itemByName](RigidGroupList_itemByName.htm) | Function that returns the specified rigid group using a name. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](RigidGroupList_count.htm) | Returns number of rigid groups in the list. |
| [isValid](RigidGroupList_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](RigidGroupList_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Occurrence.rigidGroups](Occurrence_rigidGroups.htm)

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |