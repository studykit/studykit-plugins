# FusionProductPreferences.isAutoProjectGeometry Property

Parent Object: [FusionProductPreferences](FusionProductPreferences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionProductPreferences.h>

## Description

Gets and Sets if geometry, not in the active sketch plane, is to be automatically projected.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionProductPreferences\_var" is a variable referencing a FusionProductPreferences object. |

"fusionProductPreferences\_var" is a variable referencing a FusionProductPreferences object. ```` ``` #include <Fusion/Fusion/FusionProductPreferences.h>  // Get the value of the property. boolean propertyValue = fusionProductPreferences_var->isAutoProjectGeometry();  // Set the value of the property, where value_var is a boolean. bool returnValue = fusionProductPreferences_var->isAutoProjectGeometry(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |