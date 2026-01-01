# CAMFolders Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMFolders.h>

## Description

Collection that provides access to the folders within an existing setup, folder or pattern.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addFolder](CAMFolders_addFolder.htm) | Creates a folder with the specified name and returns it as CAMFolder object. |
| [classType](CAMFolders_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](CAMFolders_item.htm) | Function that returns the specified folder using an index into the collection. |
| [itemByName](CAMFolders_itemByName.htm) | Returns the folder with the specified name (as appears in the browser). |
| [itemByOperationId](CAMFolders_itemByOperationId.htm) | Returns the folder with the specified operation id. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](CAMFolders_count.htm) | The number of items in the collection. |
| [isValid](CAMFolders_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CAMFolders_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CAMFolder.folders](CAMFolder_folders.htm), [CAMHoleRecognition.folders](CAMHoleRecognition_folders.htm), [CAMPattern.folders](CAMPattern_folders.htm), [Setup.folders](Setup_folders.htm)

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |