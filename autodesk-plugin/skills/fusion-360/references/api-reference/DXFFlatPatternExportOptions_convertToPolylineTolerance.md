# DXFFlatPatternExportOptions.convertToPolylineTolerance Property

Parent Object: [DXFFlatPatternExportOptions](DXFFlatPatternExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/DXFFlatPatternExportOptions.h>

## Description

Specifies the tolerance when converting a spline to polylines. This value is only used when the isSplineConvertedToPolyline property is true and otherwise it is ignored. The units for this value are centimeters. Defaults to 0.01 cm.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dXFFlatPatternExportOptions\_var" is a variable referencing a DXFFlatPatternExportOptions object. |

"dXFFlatPatternExportOptions\_var" is a variable referencing a DXFFlatPatternExportOptions object. ```` ``` #include <Fusion/Fusion/DXFFlatPatternExportOptions.h>  // Get the value of the property. double propertyValue = dXFFlatPatternExportOptions_var->convertToPolylineTolerance();  // Set the value of the property, where value_var is a double. bool returnValue = dXFFlatPatternExportOptions_var->convertToPolylineTolerance(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |