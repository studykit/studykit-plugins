# OBJExportOptions.filename Property

Parent Object: [OBJExportOptions](OBJExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/OBJExportOptions.h>

## Description

Gets and sets the filename that the exported file will be written to. This can be empty in the case of STL export and sending the result to the mesh editor.

## Syntax

* [Python](#Python)
* [C++](#C++)

"oBJExportOptions\_var" is a variable referencing an OBJExportOptions object. |

"oBJExportOptions\_var" is a variable referencing an OBJExportOptions object. ```` ``` #include <Fusion/Fusion/OBJExportOptions.h>  // Get the value of the property. string propertyValue = oBJExportOptions_var->filename();  // Set the value of the property, where value_var is a string. bool returnValue = oBJExportOptions_var->filename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |