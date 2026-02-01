# IGESExportOptions.filename Property

Parent Object: [IGESExportOptions](IGESExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/IGESExportOptions.h>

## Description

Gets and sets the filename that the exported file will be written to. This can be empty in the case of STL export and sending the result to the mesh editor.

## Syntax

* [Python](#Python)
* [C++](#C++)

"iGESExportOptions\_var" is a variable referencing an IGESExportOptions object. |

"iGESExportOptions\_var" is a variable referencing an IGESExportOptions object. ```` ``` #include <Fusion/Fusion/IGESExportOptions.h>  // Get the value of the property. string propertyValue = iGESExportOptions_var->filename();  // Set the value of the property, where value_var is a string. bool returnValue = iGESExportOptions_var->filename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |