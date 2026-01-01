# DXFSketchExportOptions.isConstructionExported Property

Parent Object: [DXFSketchExportOptions](DXFSketchExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/DXFSketchExportOptions.h>

## Description

Indicates if construction geometry should be exported. Defaults to true, which will export all construction geometry. If false it will be ignored and not included in the DXF file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dXFSketchExportOptions\_var" is a variable referencing a DXFSketchExportOptions object. |

"dXFSketchExportOptions\_var" is a variable referencing a DXFSketchExportOptions object. ```` ``` #include <Fusion/Fusion/DXFSketchExportOptions.h>  // Get the value of the property. boolean propertyValue = dXFSketchExportOptions_var->isConstructionExported();  // Set the value of the property, where value_var is a boolean. bool returnValue = dXFSketchExportOptions_var->isConstructionExported(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |