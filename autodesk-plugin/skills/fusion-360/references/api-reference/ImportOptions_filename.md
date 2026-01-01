# ImportOptions.filename Property

Parent Object: [ImportOptions](ImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ImportOptions.h>

## Description

Gets and sets the filename or URL of the file to be imported.

## Syntax

* [Python](#Python)
* [C++](#C++)

"importOptions\_var" is a variable referencing an ImportOptions object. |

"importOptions\_var" is a variable referencing an ImportOptions object. ```` ``` #include <Core/Application/ImportOptions.h>  // Get the value of the property. string propertyValue = importOptions_var->filename();  // Set the value of the property, where value_var is a string. bool returnValue = importOptions_var->filename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |