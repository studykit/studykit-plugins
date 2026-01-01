# DataFileFuture Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFileFuture.h>

## Description

Used to check the state and get back the results of a file upload.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](DataFileFuture_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [dataFile](DataFileFuture_dataFile.htm) | Returns the DataFile when the upload is complete (uplodeState returns UploadFinished). Returns null if the upload is still running or has failed. |
| [isValid](DataFileFuture_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](DataFileFuture_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [uploadState](DataFileFuture_uploadState.htm) | Returns the current state of the upload. |

## Accessed From

[Component.saveCopyAs](Component_saveCopyAs.htm), [DataFile.copyWithInput](DataFile_copyWithInput.htm), [DataFolder.uploadAssembly](DataFolder_uploadAssembly.htm), [DataFolder.uploadFile](DataFolder_uploadFile.htm), [FlatPatternComponent.saveCopyAs](FlatPatternComponent_saveCopyAs.htm)

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |