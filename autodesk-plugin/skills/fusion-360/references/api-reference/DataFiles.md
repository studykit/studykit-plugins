# DataFiles Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFiles.h>

## Description

Returns the items within a folder. This includes everything in a folder except for other folders.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [asArray](DataFiles_asArray.htm) | Get the current list of all files. |
| [classType](DataFiles_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](DataFiles_item.htm) | Returns the specified data file. |
| [itemById](DataFiles_itemById.htm) | Returns the file specified using the ID or version ID of the file. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](DataFiles_count.htm) | The number of data items in this collection. |
| [isValid](DataFiles_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](DataFiles_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[DataFile.childReferences](DataFile_childReferences.htm), [DataFile.parentReferences](DataFile_parentReferences.htm), [DataFile.versions](DataFile_versions.htm), [DataFolder.dataFiles](DataFolder_dataFiles.htm), [DesignDataFile.childReferences](DesignDataFile_childReferences.htm), [DesignDataFile.parentReferences](DesignDataFile_parentReferences.htm), [DesignDataFile.versions](DesignDataFile_versions.htm)

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |