# DXFFlatPatternExportOptions.filename Property

Parent Object: [DXFFlatPatternExportOptions](DXFFlatPatternExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/DXFFlatPatternExportOptions.h>

## Description

Gets and sets the filename that the exported file will be written to. This can be empty in the case of STL export and sending the result to the mesh editor.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dXFFlatPatternExportOptions\_var" is a variable referencing a DXFFlatPatternExportOptions object. |

"dXFFlatPatternExportOptions\_var" is a variable referencing a DXFFlatPatternExportOptions object. ```` ``` #include <Fusion/Fusion/DXFFlatPatternExportOptions.h>  // Get the value of the property. string propertyValue = dXFFlatPatternExportOptions_var->filename();  // Set the value of the property, where value_var is a string. bool returnValue = dXFFlatPatternExportOptions_var->filename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |