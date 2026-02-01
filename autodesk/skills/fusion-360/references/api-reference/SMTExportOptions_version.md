# SMTExportOptions.version Property

Parent Object: [SMTExportOptions](SMTExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SMTExportOptions.h>

## Description

Gets and set the version of the SMT format to write to. The default is to use the current version of the Autodesk Shape Manager kernel that Fusion is using. Specifying an invalid version will result in an assert.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sMTExportOptions\_var" is a variable referencing a SMTExportOptions object.  ```` ``` # Get the value of the property. propertyValue = sMTExportOptions_var.version  # Set the value of the property. sMTExportOptions_var.version = propertyValue ``` ```` |

"sMTExportOptions\_var" is a variable referencing a SMTExportOptions object. ```` ``` #include <Fusion/Fusion/SMTExportOptions.h>  // Get the value of the property. integer propertyValue = sMTExportOptions_var->version();  // Set the value of the property, where value_var is an integer. bool returnValue = sMTExportOptions_var->version(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |