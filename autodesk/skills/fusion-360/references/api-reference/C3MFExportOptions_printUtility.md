# C3MFExportOptions.printUtility Property

Parent Object: [C3MFExportOptions](C3MFExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/C3MFExportOptions.h>

## Description

Specifies which print utility to use when opening the 3MF file if the sendToPrintUtility property is true. The value of this property can be one of the strings returned by the availalbePrintUtilities property, which will specify one of the know print utilities. You can also specify a custom print utility by specifying the full path to the print utility executable. The default value of this property is the last setting specified in the user-interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"c3MFExportOptions\_var" is a variable referencing a C3MFExportOptions object. |

"c3MFExportOptions\_var" is a variable referencing a C3MFExportOptions object. ```` ``` #include <Fusion/Fusion/C3MFExportOptions.h>  // Get the value of the property. string propertyValue = c3MFExportOptions_var->printUtility();  // Set the value of the property, where value_var is a string. bool returnValue = c3MFExportOptions_var->printUtility(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |