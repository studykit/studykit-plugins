# DXFSketchExportOptions.isProjectedGeometryExported Property

Parent Object: [DXFSketchExportOptions](DXFSketchExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/DXFSketchExportOptions.h>

## Description

Indicates if any projected geometry should be exported. Defaults to true, which will export all projected geometry. If false it will be ignored and not included in the DXF file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dXFSketchExportOptions\_var" is a variable referencing a DXFSketchExportOptions object. |

"dXFSketchExportOptions\_var" is a variable referencing a DXFSketchExportOptions object. ```` ``` #include <Fusion/Fusion/DXFSketchExportOptions.h>  // Get the value of the property. boolean propertyValue = dXFSketchExportOptions_var->isProjectedGeometryExported();  // Set the value of the property, where value_var is a boolean. bool returnValue = dXFSketchExportOptions_var->isProjectedGeometryExported(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |