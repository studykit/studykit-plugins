# DrawingExportManager Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/DrawingExportManager.h>

## Description

Provides support to export the drawing in various formats.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](DrawingExportManager_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createPDFExportOptions](DrawingExportManager_createPDFExportOptions.htm) | Defines the various settings for a STEP export. |
| [execute](DrawingExportManager_execute.htm) | Executes the export operation to create the file in the format specified by the input ExportOptions object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](DrawingExportManager_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](DrawingExportManager_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Drawing.exportManager](Drawing_exportManager.htm)

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |