# IGESImportOptions.filename Property

Parent Object: [IGESImportOptions](IGESImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/IGESImportOptions.h>

## Description

Gets and sets the filename or URL of the file to be imported.

## Syntax

* [Python](#Python)
* [C++](#C++)

"iGESImportOptions\_var" is a variable referencing an IGESImportOptions object. |

"iGESImportOptions\_var" is a variable referencing an IGESImportOptions object. ```` ``` #include <Core/Application/IGESImportOptions.h>  // Get the value of the property. string propertyValue = iGESImportOptions_var->filename();  // Set the value of the property, where value_var is a string. bool returnValue = iGESImportOptions_var->filename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |