# FusionArchiveExportOptions.objectType Property

Parent Object: [FusionArchiveExportOptions](FusionArchiveExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionArchiveExportOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionArchiveExportOptions\_var" is a variable referencing a FusionArchiveExportOptions object.  ```` ``` # Get the value of the property. propertyValue = fusionArchiveExportOptions_var.objectType ``` ```` |

"fusionArchiveExportOptions\_var" is a variable referencing a FusionArchiveExportOptions object. ```` ``` #include <Fusion/Fusion/FusionArchiveExportOptions.h>  // Get the value of the property. string propertyValue = fusionArchiveExportOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |