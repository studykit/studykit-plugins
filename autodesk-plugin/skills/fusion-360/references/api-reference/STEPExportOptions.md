# STEPExportOptions Object

Derived from: [ExportOptions](ExportOptions.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/STEPExportOptions.h>

## Description

Defines that a STEP export is to be done and specifies the various options.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](STEPExportOptions_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [filename](STEPExportOptions_filename.htm) | Gets and sets the filename that the exported file will be written to. This can be empty in the case of STL export and sending the result to the mesh editor. |
| [geometry](STEPExportOptions_geometry.htm) | Specifies the geometry to export. This can be an Occurrence, or the root Component. For STL, OBJ, and 3MF export, it can be a BRepBody. For DXF export, it can be a sketch of flat pattern. |
| [isValid](STEPExportOptions_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](STEPExportOptions_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [wantTempIds](STEPExportOptions_wantTempIds.htm) | Indicates if the STEP file should include the Fusion temporary IDs for faces and edges. Outside services can use these IDs with the findByTempId method of the BRepBody, which will return the given entity. The default is false. |

## Accessed From

[ExportManager.createSTEPExportOptions](ExportManager_createSTEPExportOptions.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [ExportManager API Sample](ExportManager_Sample.htm) | Demonstrates how to export f3d to different formats. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |