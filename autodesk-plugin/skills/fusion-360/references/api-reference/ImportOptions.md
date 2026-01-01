# ImportOptions Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/ImportOptions.h>

## Description

The base class for the different import types. This class is never directly used in an import because you need the specific import type to specify the type of import to be performed.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ImportOptions_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [filename](ImportOptions_filename.htm) | Gets and sets the filename or URL of the file to be imported. |
| [isValid](ImportOptions_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isViewFit](ImportOptions_isViewFit.htm) | Specifies if the camera should be adjusted to fit the geometry of the import. This defaults to true, which will cause a change in the current view. Setting this to false will leave the view as-is and just import the geometry. |
| [objectType](ImportOptions_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Derived Classes

[DXF2DImportOptions](DXF2DImportOptions.htm), [FusionArchiveImportOptions](FusionArchiveImportOptions.htm), [IGESImportOptions](IGESImportOptions.htm), [SATImportOptions](SATImportOptions.htm), [SMTImportOptions](SMTImportOptions.htm), [STEPImportOptions](STEPImportOptions.htm), [SVGImportOptions](SVGImportOptions.htm)

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |