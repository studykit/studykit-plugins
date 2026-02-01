# SMTExportOptions.filename Property

Parent Object: [SMTExportOptions](SMTExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SMTExportOptions.h>

## Description

Gets and sets the filename that the exported file will be written to. This can be empty in the case of STL export and sending the result to the mesh editor.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sMTExportOptions\_var" is a variable referencing a SMTExportOptions object. |

"sMTExportOptions\_var" is a variable referencing a SMTExportOptions object. ```` ``` #include <Fusion/Fusion/SMTExportOptions.h>  // Get the value of the property. string propertyValue = sMTExportOptions_var->filename();  // Set the value of the property, where value_var is a string. bool returnValue = sMTExportOptions_var->filename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |