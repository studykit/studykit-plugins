# CAMExportManager Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMExportManager.h>

## Description

Export manager used to export the setup's models in one of the formats defined the ExportOptions objects. The export is currently restricted to additive setups only and the availability of the export option and its settings depends on the chosen machine.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CAMExportManager_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create3MFOptions](CAMExportManager_create3MFOptions.htm) | Creates a new 3MF export option. |
| [createCAMAdditiveBuildExportOptions](CAMExportManager_createCAMAdditiveBuildExportOptions.htm) | Creates a new export option based on the print setting's export formats. FFF and DED machines are not supported, their export files are generated using posts. |
| [execute](CAMExportManager_execute.htm) | Executes an export based on the export options. |
| [executeWithExportFuture](CAMExportManager_executeWithExportFuture.htm) | Executes an export based on the export options |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](CAMExportManager_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CAMExportManager_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CAM.exportManager](CAM_exportManager.htm)

## Version

Introduced in version November 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |