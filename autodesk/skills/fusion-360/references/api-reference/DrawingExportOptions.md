# DrawingExportOptions Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/DrawingExportOptions.h>

## Description

The base class for the different drawing export types. This class is never directly used in an export because you need the specific export type to specify the type of export to be performed.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](DrawingExportOptions_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [filename](DrawingExportOptions_filename.htm) | Gets and sets the filename that the exported file will be written to. |
| [isValid](DrawingExportOptions_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](DrawingExportOptions_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Derived Classes

[PDFExportOptions](PDFExportOptions.htm)

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |