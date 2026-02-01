# CAMAdditiveBuildExportFilter Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMAdditiveBuildExportFilter.h>

## Description

Export filter used by CAMAdditiveMachineBuildFileExportOptions.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CAMAdditiveBuildExportFilter_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [extension](CAMAdditiveBuildExportFilter_extension.htm) | The extension of the file format, including a leading "." |
| [id](CAMAdditiveBuildExportFilter_id.htm) | The id of the file format. |
| [isMultiFileExport](CAMAdditiveBuildExportFilter_isMultiFileExport.htm) | True if the export outputs multiple files. If so, fullFilename should point to a directory, not a file. |
| [isValid](CAMAdditiveBuildExportFilter_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](CAMAdditiveBuildExportFilter_name.htm) | The name of the file format. Might indicate whether a file format is binary or not. |
| [objectType](CAMAdditiveBuildExportFilter_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CAMAdditiveBuildExportOptions.exportFilters](CAMAdditiveBuildExportOptions_exportFilters.htm)

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |