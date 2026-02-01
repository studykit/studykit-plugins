# DXFSketchExportOptions.units Property

Parent Object: [DXFSketchExportOptions](DXFSketchExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/DXFSketchExportOptions.h>

## Description

Gets and sets the units that will be used for the DXF file. This defaults to be the same as the default units of the design.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dXFSketchExportOptions\_var" is a variable referencing a DXFSketchExportOptions object. |

"dXFSketchExportOptions\_var" is a variable referencing a DXFSketchExportOptions object. ```` ``` #include <Fusion/Fusion/DXFSketchExportOptions.h>  // Get the value of the property. DistanceUnits propertyValue = dXFSketchExportOptions_var->units();  // Set the value of the property, where value_var is a DistanceUnits. bool returnValue = dXFSketchExportOptions_var->units(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [DistanceUnits](DistanceUnits.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |