# FusionArchiveImportOptions.filename Property

Parent Object: [FusionArchiveImportOptions](FusionArchiveImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/FusionArchiveImportOptions.h>

## Description

Gets and sets the filename or URL of the file to be imported.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionArchiveImportOptions\_var" is a variable referencing a FusionArchiveImportOptions object. |

"fusionArchiveImportOptions\_var" is a variable referencing a FusionArchiveImportOptions object. ```` ``` #include <Core/Application/FusionArchiveImportOptions.h>  // Get the value of the property. string propertyValue = fusionArchiveImportOptions_var->filename();  // Set the value of the property, where value_var is a string. bool returnValue = fusionArchiveImportOptions_var->filename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |