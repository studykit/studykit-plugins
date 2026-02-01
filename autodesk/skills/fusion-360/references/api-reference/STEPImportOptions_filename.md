# STEPImportOptions.filename Property

Parent Object: [STEPImportOptions](STEPImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/STEPImportOptions.h>

## Description

Gets and sets the filename or URL of the file to be imported.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sTEPImportOptions\_var" is a variable referencing a STEPImportOptions object. |

"sTEPImportOptions\_var" is a variable referencing a STEPImportOptions object. ```` ``` #include <Core/Application/STEPImportOptions.h>  // Get the value of the property. string propertyValue = sTEPImportOptions_var->filename();  // Set the value of the property, where value_var is a string. bool returnValue = sTEPImportOptions_var->filename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |