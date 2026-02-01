# OBJExportOptions.availablePrintUtilities Property

Parent Object: [OBJExportOptions](OBJExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/OBJExportOptions.h>

## Description

Returns a list of the known available print utilities. These strings can be used to set the PrintUtility property to specify which print utility to open the OBJ file in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"oBJExportOptions\_var" is a variable referencing an OBJExportOptions object. |

"oBJExportOptions\_var" is a variable referencing an OBJExportOptions object. ```` ``` #include <Fusion/Fusion/OBJExportOptions.h>  // Get the value of the property. std::vector<string> propertyValue = oBJExportOptions_var->availablePrintUtilities(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type string.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |