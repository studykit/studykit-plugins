# DXFFlatPatternExportOptions Object

Derived from: [ExportOptions](ExportOptions.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/DXFFlatPatternExportOptions.h>

## Description

Defines that a DXF export of a flat pattern is to be done and specifies the various options.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](DXFFlatPatternExportOptions_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [convertToPolylineTolerance](DXFFlatPatternExportOptions_convertToPolylineTolerance.htm) | Specifies the tolerance when converting a spline to polylines. This value is only used when the isSplineConvertedToPolyline property is true and otherwise it is ignored. The units for this value are centimeters. Defaults to 0.01 cm. |
| [filename](DXFFlatPatternExportOptions_filename.htm) | Gets and sets the filename that the exported file will be written to. This can be empty in the case of STL export and sending the result to the mesh editor. |
| [geometry](DXFFlatPatternExportOptions_geometry.htm) | Specifies the geometry to export. This can be an Occurrence, or the root Component. For STL, OBJ, and 3MF export, it can be a BRepBody. For DXF export, it can be a sketch of flat pattern. |
| [isCenterLinesExported](DXFFlatPatternExportOptions_isCenterLinesExported.htm) | Specifies if the center lines (bend line) of the flat pattern are exported in the DXF. Defaults to true. |
| [isExtentLinesExported](DXFFlatPatternExportOptions_isExtentLinesExported.htm) | Specifies if the bend extent lines of the flat pattern are exported in the DXF. Defaults to true. |
| [isSplineConvertedToPolyline](DXFFlatPatternExportOptions_isSplineConvertedToPolyline.htm) | Specifies if splines are converted to polylines. If true, the convertToPolylineTolerance value is used to specify the accuracy of the conversion. Defaults to false. |
| [isValid](DXFFlatPatternExportOptions_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](DXFFlatPatternExportOptions_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [units](DXFFlatPatternExportOptions_units.htm) | Gets and sets the units that will be used for the DXF file. This defaults to be the same as the default units of the design. |

## Accessed From

[ExportManager.createDXFFlatPatternExportOptions](ExportManager_createDXFFlatPatternExportOptions.htm)

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |