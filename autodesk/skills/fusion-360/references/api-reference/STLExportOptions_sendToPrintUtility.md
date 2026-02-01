# STLExportOptions.sendToPrintUtility Property

Parent Object: [STLExportOptions](STLExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/STLExportOptions.h>

## Description

Gets and sets whether the created STL file will be sent to the print utility specified by the printUtility property. If this is false a filename must be defined.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sTLExportOptions\_var" is a variable referencing a STLExportOptions object. |

"sTLExportOptions\_var" is a variable referencing a STLExportOptions object. ```` ``` #include <Fusion/Fusion/STLExportOptions.h>  // Get the value of the property. boolean propertyValue = sTLExportOptions_var->sendToPrintUtility();  // Set the value of the property, where value_var is a boolean. bool returnValue = sTLExportOptions_var->sendToPrintUtility(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

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