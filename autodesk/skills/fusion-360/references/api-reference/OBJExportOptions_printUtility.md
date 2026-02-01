# OBJExportOptions.printUtility Property

Parent Object: [OBJExportOptions](OBJExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/OBJExportOptions.h>

## Description

Specifies which print utility to use when opening the OBJ file if the sendToPrintUtility property is true. The value of this property can be one of the strings returned by the availalbePrintUtilities property, which will specify one of the known print utilities. You can also specify a custom print utility by specifying the full path to the print utility executable. The default value of this property is the last setting specified in the user-interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"oBJExportOptions\_var" is a variable referencing an OBJExportOptions object. |

"oBJExportOptions\_var" is a variable referencing an OBJExportOptions object. ```` ``` #include <Fusion/Fusion/OBJExportOptions.h>  // Get the value of the property. string propertyValue = oBJExportOptions_var->printUtility();  // Set the value of the property, where value_var is a string. bool returnValue = oBJExportOptions_var->printUtility(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |