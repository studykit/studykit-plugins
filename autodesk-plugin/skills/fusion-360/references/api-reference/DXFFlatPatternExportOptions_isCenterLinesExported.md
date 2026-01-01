# DXFFlatPatternExportOptions.isCenterLinesExported Property

Parent Object: [DXFFlatPatternExportOptions](DXFFlatPatternExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/DXFFlatPatternExportOptions.h>

## Description

Specifies if the center lines (bend line) of the flat pattern are exported in the DXF. Defaults to true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dXFFlatPatternExportOptions\_var" is a variable referencing a DXFFlatPatternExportOptions object. |

"dXFFlatPatternExportOptions\_var" is a variable referencing a DXFFlatPatternExportOptions object. ```` ``` #include <Fusion/Fusion/DXFFlatPatternExportOptions.h>  // Get the value of the property. boolean propertyValue = dXFFlatPatternExportOptions_var->isCenterLinesExported();  // Set the value of the property, where value_var is a boolean. bool returnValue = dXFFlatPatternExportOptions_var->isCenterLinesExported(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |