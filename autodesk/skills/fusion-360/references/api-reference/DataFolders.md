# DataFolders Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFolders.h>

## Description

Collection object the provides a list of data folders.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](DataFolders_add.htm) | Creates a new folder within the parent folder. |
| [asArray](DataFolders_asArray.htm) | Get the current list of all folders. |
| [classType](DataFolders_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](DataFolders_item.htm) | Returns the specified folder. |
| [itemById](DataFolders_itemById.htm) | Returns the folder specified using the ID of the folder. |
| [itemByName](DataFolders_itemByName.htm) | Returns the folder specified using the name of the folder. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](DataFolders_count.htm) | The number of folders in this collection. |
| [isValid](DataFolders_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](DataFolders_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[DataFolder.dataFolders](DataFolder_dataFolders.htm)

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |