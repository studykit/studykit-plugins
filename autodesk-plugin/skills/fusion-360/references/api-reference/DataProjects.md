# DataProjects Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataProjects.h>

## Description

Collection object that provides a list of all available projects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](DataProjects_add.htm) | Creates a new project in the parent hub. |
| [asArray](DataProjects_asArray.htm) | Get the current list of all projects. |
| [classType](DataProjects_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](DataProjects_item.htm) | Returns the specified project. |
| [itemById](DataProjects_itemById.htm) | Returns the project specified using the ID of the project. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](DataProjects_count.htm) | The number of projects in this collection. |
| [isValid](DataProjects_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](DataProjects_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Data.dataProjects](Data_dataProjects.htm), [DataHub.dataProjects](DataHub_dataProjects.htm)

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |