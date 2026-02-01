# SMTImportOptions.filename Property

Parent Object: [SMTImportOptions](SMTImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SMTImportOptions.h>

## Description

Gets and sets the filename or URL of the file to be imported.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sMTImportOptions\_var" is a variable referencing a SMTImportOptions object. |

"sMTImportOptions\_var" is a variable referencing a SMTImportOptions object. ```` ``` #include <Core/Application/SMTImportOptions.h>  // Get the value of the property. string propertyValue = sMTImportOptions_var->filename();  // Set the value of the property, where value_var is a string. bool returnValue = sMTImportOptions_var->filename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |