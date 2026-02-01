# CAMExportFuture Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMExportFuture.h>

## Description

Used to check the state and get back the results of an operation generation.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CAMExportFuture_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [error](CAMExportFuture_error.htm) | Gets the last encountered error message generated on the export thread. |
| [exportOptions](CAMExportFuture_exportOptions.htm) | Returns the export option used to define the export associated with this future object. |
| [isGenerationCompleted](CAMExportFuture_isGenerationCompleted.htm) | Returns true if the export has finished generating. |
| [isValid](CAMExportFuture_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CAMExportFuture_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [progress](CAMExportFuture_progress.htm) | Returns the progress as a percentage value between 0.0% and 100.0%. |
| [warning](CAMExportFuture_warning.htm) | Gets the last encountered warning message generated on the export thread. |

## Accessed From

[CAMExportManager.executeWithExportFuture](CAMExportManager_executeWithExportFuture.htm)

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |