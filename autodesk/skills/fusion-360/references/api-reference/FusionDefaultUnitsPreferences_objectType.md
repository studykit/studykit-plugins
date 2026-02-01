# FusionDefaultUnitsPreferences.objectType Property

Parent Object: [FusionDefaultUnitsPreferences](FusionDefaultUnitsPreferences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionDefaultUnitsPreferences.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionDefaultUnitsPreferences\_var" is a variable referencing a FusionDefaultUnitsPreferences object.  ```` ``` # Get the value of the property. propertyValue = fusionDefaultUnitsPreferences_var.objectType ``` ```` |

"fusionDefaultUnitsPreferences\_var" is a variable referencing a FusionDefaultUnitsPreferences object. ```` ``` #include <Fusion/Fusion/FusionDefaultUnitsPreferences.h>  // Get the value of the property. string propertyValue = fusionDefaultUnitsPreferences_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |