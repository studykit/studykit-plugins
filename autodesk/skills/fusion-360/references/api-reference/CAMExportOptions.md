# CAMExportOptions Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMExportOptions.h>

## Description

Parent class for all ExportOptions objects giving access to the setup and file name used for the export.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CAMExportOptions_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [error](CAMExportOptions_error.htm) | Gets the last encountered error message. When the CAMExportManager's executeWithExportFuture() method is used, this method only returns errors encoutered when setting up the export. Errors thrown afterwards can be retrieved via the CAMExportFuture object. When the CAMExportManager's execute() method is used, any error can be retrieved using this property. |
| [exportObject](CAMExportOptions_exportObject.htm) | The export object we want to export. Depending on the actual export option, this might be geometry, an operation or a setup. |
| [fullFilename](CAMExportOptions_fullFilename.htm) | The file we want to export to. Needs to contain a valid path, as no intermediate folders are created. |
| [isThumbnailSupported](CAMExportOptions_isThumbnailSupported.htm) | Method to check if the exporter implementation supports thumbnail |
| [isValid](CAMExportOptions_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CAMExportOptions_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [thumbnailPath](CAMExportOptions_thumbnailPath.htm) | Path to the thumbnail for the buildfile |

## Accessed From

[CAMExportFuture.exportOptions](CAMExportFuture_exportOptions.htm)

## Derived Classes

[CAM3MFExportOptions](CAM3MFExportOptions.htm), [CAMAdditiveBuildExportOptions](CAMAdditiveBuildExportOptions.htm)

## Version

Introduced in version November 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |