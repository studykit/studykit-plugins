# STLExportOptions.printUtility Property

Parent Object: [STLExportOptions](STLExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/STLExportOptions.h>

## Description

Specifies which print utility to use when opening the STL file if the sendToPrintUtility property is true. The value of this property can be one of the strings returned by the availalbePrintUtilities property, which will specify one of the know print utilities. You can also specify a custom print utility by specifying the full path to the print utility executable. The default value of this property is the last setting specified in the user-interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sTLExportOptions\_var" is a variable referencing a STLExportOptions object. |

"sTLExportOptions\_var" is a variable referencing a STLExportOptions object. ```` ``` #include <Fusion/Fusion/STLExportOptions.h>  // Get the value of the property. string propertyValue = sTLExportOptions_var->printUtility();  // Set the value of the property, where value_var is a string. bool returnValue = sTLExportOptions_var->printUtility(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

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