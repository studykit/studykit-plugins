# FusionArchiveImportOptions.objectType Property

Parent Object: [FusionArchiveImportOptions](FusionArchiveImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/FusionArchiveImportOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionArchiveImportOptions\_var" is a variable referencing a FusionArchiveImportOptions object.  ```` ``` # Get the value of the property. propertyValue = fusionArchiveImportOptions_var.objectType ``` ```` |

"fusionArchiveImportOptions\_var" is a variable referencing a FusionArchiveImportOptions object. ```` ``` #include <Core/Application/FusionArchiveImportOptions.h>  // Get the value of the property. string propertyValue = fusionArchiveImportOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |