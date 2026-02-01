# SATImportOptions.filename Property

Parent Object: [SATImportOptions](SATImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SATImportOptions.h>

## Description

Gets and sets the filename or URL of the file to be imported.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sATImportOptions\_var" is a variable referencing a SATImportOptions object. |

"sATImportOptions\_var" is a variable referencing a SATImportOptions object. ```` ``` #include <Core/Application/SATImportOptions.h>  // Get the value of the property. string propertyValue = sATImportOptions_var->filename();  // Set the value of the property, where value_var is a string. bool returnValue = sATImportOptions_var->filename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |