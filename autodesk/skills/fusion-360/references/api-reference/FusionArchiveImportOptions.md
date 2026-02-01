# FusionArchiveImportOptions Object

Derived from: [ImportOptions](ImportOptions.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/FusionArchiveImportOptions.h>

## Description

Defines that a Fusion Archive import is to be done and specifies the various options.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](FusionArchiveImportOptions_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [filename](FusionArchiveImportOptions_filename.htm) | Gets and sets the filename or URL of the file to be imported. |
| [isValid](FusionArchiveImportOptions_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isViewFit](FusionArchiveImportOptions_isViewFit.htm) | Specifies if the camera should be adjusted to fit the geometry of the import. This defaults to true, which will cause a change in the current view. Setting this to false will leave the view as-is and just import the geometry. |
| [objectType](FusionArchiveImportOptions_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[ImportManager.createFusionArchiveImportOptions](ImportManager_createFusionArchiveImportOptions.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Import Manager API Sample](ImportManager_Sample.htm) | Demonstrates how to import different formats to Fusion document |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |