# C3MFExportOptions.sendToPrintUtility Property

Parent Object: [C3MFExportOptions](C3MFExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/C3MFExportOptions.h>

## Description

Gets and sets whether the created 3MF file will be sent to the print utility specified by the printUtility property. If this is false a filename must be defined.

## Syntax

* [Python](#Python)
* [C++](#C++)

"c3MFExportOptions\_var" is a variable referencing a C3MFExportOptions object. |

"c3MFExportOptions\_var" is a variable referencing a C3MFExportOptions object. ```` ``` #include <Fusion/Fusion/C3MFExportOptions.h>  // Get the value of the property. boolean propertyValue = c3MFExportOptions_var->sendToPrintUtility();  // Set the value of the property, where value_var is a boolean. bool returnValue = c3MFExportOptions_var->sendToPrintUtility(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |