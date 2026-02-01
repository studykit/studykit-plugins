# STLExportOptions.availablePrintUtilities Property

Parent Object: [STLExportOptions](STLExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/STLExportOptions.h>

## Description

Returns a list of the known available print utilities. These strings can be used to set the PrintUtility property to specify which print utility to open the STL file in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sTLExportOptions\_var" is a variable referencing a STLExportOptions object. |

"sTLExportOptions\_var" is a variable referencing a STLExportOptions object. ```` ``` #include <Fusion/Fusion/STLExportOptions.h>  // Get the value of the property. std::vector<string> propertyValue = sTLExportOptions_var->availablePrintUtilities(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [STLExport API Sample](STLExport_Sample.htm) | Demonstrates how to export f3d to STL format. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |