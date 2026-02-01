# SATExportOptions.filename Property

Parent Object: [SATExportOptions](SATExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SATExportOptions.h>

## Description

Gets and sets the filename that the exported file will be written to. This can be empty in the case of STL export and sending the result to the mesh editor.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sATExportOptions\_var" is a variable referencing a SATExportOptions object. |

"sATExportOptions\_var" is a variable referencing a SATExportOptions object. ```` ``` #include <Fusion/Fusion/SATExportOptions.h>  // Get the value of the property. string propertyValue = sATExportOptions_var->filename();  // Set the value of the property, where value_var is a string. bool returnValue = sATExportOptions_var->filename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |