# DXFFlatPatternExportOptions.isSplineConvertedToPolyline Property

Parent Object: [DXFFlatPatternExportOptions](DXFFlatPatternExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/DXFFlatPatternExportOptions.h>

## Description

Specifies if splines are converted to polylines. If true, the convertToPolylineTolerance value is used to specify the accuracy of the conversion. Defaults to false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dXFFlatPatternExportOptions\_var" is a variable referencing a DXFFlatPatternExportOptions object. |

"dXFFlatPatternExportOptions\_var" is a variable referencing a DXFFlatPatternExportOptions object. ```` ``` #include <Fusion/Fusion/DXFFlatPatternExportOptions.h>  // Get the value of the property. boolean propertyValue = dXFFlatPatternExportOptions_var->isSplineConvertedToPolyline();  // Set the value of the property, where value_var is a boolean. bool returnValue = dXFFlatPatternExportOptions_var->isSplineConvertedToPolyline(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |