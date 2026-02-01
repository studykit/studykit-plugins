# DXFFlatPatternExportOptions.units Property

Parent Object: [DXFFlatPatternExportOptions](DXFFlatPatternExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/DXFFlatPatternExportOptions.h>

## Description

Gets and sets the units that will be used for the DXF file. This defaults to be the same as the default units of the design.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dXFFlatPatternExportOptions\_var" is a variable referencing a DXFFlatPatternExportOptions object. |

"dXFFlatPatternExportOptions\_var" is a variable referencing a DXFFlatPatternExportOptions object. ```` ``` #include <Fusion/Fusion/DXFFlatPatternExportOptions.h>  // Get the value of the property. DistanceUnits propertyValue = dXFFlatPatternExportOptions_var->units();  // Set the value of the property, where value_var is a DistanceUnits. bool returnValue = dXFFlatPatternExportOptions_var->units(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [DistanceUnits](DistanceUnits.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |