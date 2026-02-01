# ChildOperationList Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/CAM/ChildOperationList.h>

## Description

Provides access to the collection of child operations, folders and patterns of an existing setup.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ChildOperationList_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](ChildOperationList_item.htm) | Returns the specified item using an index into the collection. |
| [itemByName](ChildOperationList_itemByName.htm) | Returns the operation, folder or pattern with the specified name (the name seen in the browser). |
| [itemByOperationId](ChildOperationList_itemByOperationId.htm) | Returns the operation, folder or pattern with the specified operation id. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ChildOperationList_count.htm) | Gets the number of objects in the collection. |
| [isValid](ChildOperationList_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ChildOperationList_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CAMFolder.children](CAMFolder_children.htm), [CAMHoleRecognition.children](CAMHoleRecognition_children.htm), [CAMPattern.children](CAMPattern_children.htm), [Setup.children](Setup_children.htm)

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |