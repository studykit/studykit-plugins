# Milestone Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/Milestone.h>

## Description

An object that represents a milestone.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Milestone_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](Milestone_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](Milestone_name.htm) | Gets and sets the name of the milestone. |
| [objectType](Milestone_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [version](Milestone_version.htm) | Returns the file version associated with this milestone. |

## Accessed From

[DataFile.createMilestone](DataFile_createMilestone.htm), [DataFile.milestone](DataFile_milestone.htm), [DesignDataFile.createMilestone](DesignDataFile_createMilestone.htm), [DesignDataFile.milestone](DesignDataFile_milestone.htm), [Milestones.asArray](Milestones_asArray.htm), [Milestones.item](Milestones_item.htm), [Milestones.itemByName](Milestones_itemByName.htm)

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |