# C3MFExportOptions.availablePrintUtilities Property

Parent Object: [C3MFExportOptions](C3MFExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/C3MFExportOptions.h>

## Description

Returns a list of the known available print utilities. These strings can be used to set the PrintUtility property to specify which print utility to open the 3MF file in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"c3MFExportOptions\_var" is a variable referencing a C3MFExportOptions object. |

"c3MFExportOptions\_var" is a variable referencing a C3MFExportOptions object. ```` ``` #include <Fusion/Fusion/C3MFExportOptions.h>  // Get the value of the property. std::vector<string> propertyValue = c3MFExportOptions_var->availablePrintUtilities(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type string.

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |