# Milestones Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/Milestones.h>

## Description

Returns the milestones associated with a DataFile.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [asArray](Milestones_asArray.htm) | Get the current list of all milestones. |
| [classType](Milestones_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](Milestones_item.htm) | Returns the specified milestone. |
| [itemByName](Milestones_itemByName.htm) | Returns the milestone specified using its name.. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](Milestones_count.htm) | The number of data items in this collection. |
| [isValid](Milestones_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Milestones_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[DataFile.milestones](DataFile_milestones.htm), [DesignDataFile.milestones](DesignDataFile_milestones.htm)

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |