# DataObjectFuture Object

Derived from: [Future](Future.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataObjectFuture.h>

## Description

Used to check the state of getting data associated with an object where the associated data typically exists on the cloud.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](DataObjectFuture_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [dataObject](DataObjectFuture_dataObject.htm) | Returns the DataObject when the data has become available, (state returns FinishedFutureState). Returns null if the operation is still running or has failed. |
| [isValid](DataObjectFuture_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](DataObjectFuture_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [state](DataObjectFuture_state.htm) | Returns the current state of the process associated with this future. |

## Accessed From

[DataFile.dataObject](DataFile_dataObject.htm)

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |