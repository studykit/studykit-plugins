# DataProject Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataProject.h>

## Description

Represents the master branch project within a hub.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](DataProject_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [id](DataProject_id.htm) | Returns the unique ID for this project. This is the same id used in the APS Data Management API in an unencoded form and will look something like this: "a.45637". |
| [isValid](DataProject_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](DataProject_name.htm) | Gets and sets the name of the project. |
| [objectType](DataProject_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentHub](DataProject_parentHub.htm) | Returns the parent DataHub of this project. |
| [rootFolder](DataProject_rootFolder.htm) | Returns the project's root folder. This provides access to all of the folders and the files in the top level of the project. |

## Accessed From

[Data.activeProject](Data_activeProject.htm), [DataFile.parentProject](DataFile_parentProject.htm), [DataFolder.parentProject](DataFolder_parentProject.htm), [DataProjects.add](DataProjects_add.htm), [DataProjects.asArray](DataProjects_asArray.htm), [DataProjects.item](DataProjects_item.htm), [DataProjects.itemById](DataProjects_itemById.htm), [DesignDataFile.parentProject](DesignDataFile_parentProject.htm)

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |