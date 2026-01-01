# FusionUnitsManager.objectType Property

Parent Object: [FusionUnitsManager](FusionUnitsManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionUnitsManager.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionUnitsManager\_var" is a variable referencing a FusionUnitsManager object.  ```` ``` # Get the value of the property. propertyValue = fusionUnitsManager_var.objectType ``` ```` |

"fusionUnitsManager\_var" is a variable referencing a FusionUnitsManager object. ```` ``` #include <Fusion/Fusion/FusionUnitsManager.h>  // Get the value of the property. string propertyValue = fusionUnitsManager_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |