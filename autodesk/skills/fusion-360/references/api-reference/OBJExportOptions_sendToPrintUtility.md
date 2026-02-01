# OBJExportOptions.sendToPrintUtility Property

Parent Object: [OBJExportOptions](OBJExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/OBJExportOptions.h>

## Description

Gets and sets whether the created OBJ file will be sent to the print utility specified by the printUtility property. If this is false a filename must be defined. The default is false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"oBJExportOptions\_var" is a variable referencing an OBJExportOptions object. |

"oBJExportOptions\_var" is a variable referencing an OBJExportOptions object. ```` ``` #include <Fusion/Fusion/OBJExportOptions.h>  // Get the value of the property. boolean propertyValue = oBJExportOptions_var->sendToPrintUtility();  // Set the value of the property, where value_var is a boolean. bool returnValue = oBJExportOptions_var->sendToPrintUtility(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |