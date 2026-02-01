# ExportOptions Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ExportOptions.h>

## Description

The base class for the different export types. This class is never directly used in an export because you need the specific export type to specify the type of export to be performed.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ExportOptions_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [filename](ExportOptions_filename.htm) | Gets and sets the filename that the exported file will be written to. This can be empty in the case of STL export and sending the result to the mesh editor. |
| [geometry](ExportOptions_geometry.htm) | Specifies the geometry to export. This can be an Occurrence, or the root Component. For STL, OBJ, and 3MF export, it can be a BRepBody. For DXF export, it can be a sketch of flat pattern. |
| [isValid](ExportOptions_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ExportOptions_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Derived Classes

[C3MFExportOptions](C3MFExportOptions.htm), [DXFFlatPatternExportOptions](DXFFlatPatternExportOptions.htm), [DXFSketchExportOptions](DXFSketchExportOptions.htm), [FusionArchiveExportOptions](FusionArchiveExportOptions.htm), [IGESExportOptions](IGESExportOptions.htm), [OBJExportOptions](OBJExportOptions.htm), [SATExportOptions](SATExportOptions.htm), [SMTExportOptions](SMTExportOptions.htm), [STEPExportOptions](STEPExportOptions.htm), [STLExportOptions](STLExportOptions.htm), [USDExportOptions](USDExportOptions.htm)

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |