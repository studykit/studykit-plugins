# SMTExportOptions Object

Derived from: [ExportOptions](ExportOptions.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SMTExportOptions.h>

## Description

Defines that an SMT export is to be done and specifies the various options.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](SMTExportOptions_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [filename](SMTExportOptions_filename.htm) | Gets and sets the filename that the exported file will be written to. This can be empty in the case of STL export and sending the result to the mesh editor. |
| [geometry](SMTExportOptions_geometry.htm) | Specifies the geometry to export. This can be an Occurrence, or the root Component. For STL, OBJ, and 3MF export, it can be a BRepBody. For DXF export, it can be a sketch of flat pattern. |
| [isValid](SMTExportOptions_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](SMTExportOptions_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [version](SMTExportOptions_version.htm) | Gets and set the version of the SMT format to write to. The default is to use the current version of the Autodesk Shape Manager kernel that Fusion is using. Specifying an invalid version will result in an assert.   Valid versions are 218 up to the current version, which is what this property returns by default when a new SMTExportOptions object is created. |

## Accessed From

[ExportManager.createSMTExportOptions](ExportManager_createSMTExportOptions.htm)

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