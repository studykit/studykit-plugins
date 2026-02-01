# STLExportOptions.isOneFilePerBody Property

Parent Object: [STLExportOptions](STLExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/STLExportOptions.h>

## Description

If the input is an Occurrence or the root Component, this specifies if a single file should be created containing all of the bodies within that occurrence or component or if multiple files should be created; one for each body. If multiple files are created, the body name is appended to the filename. The default is false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sTLExportOptions\_var" is a variable referencing a STLExportOptions object. |

"sTLExportOptions\_var" is a variable referencing a STLExportOptions object. ```` ``` #include <Fusion/Fusion/STLExportOptions.h>  // Get the value of the property. boolean propertyValue = sTLExportOptions_var->isOneFilePerBody();  // Set the value of the property, where value_var is a boolean. bool returnValue = sTLExportOptions_var->isOneFilePerBody(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |