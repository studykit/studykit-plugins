# FusionProductPreferences.isAutoProjectEdgesOnReference Property

Parent Object: [FusionProductPreferences](FusionProductPreferences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionProductPreferences.h>

## Description

Gets and sets if model edges should be automatically projected when creating constraints and dimensions in the active sketch when the orientation is normal to the active sketch plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionProductPreferences\_var" is a variable referencing a FusionProductPreferences object. |

"fusionProductPreferences\_var" is a variable referencing a FusionProductPreferences object. ```` ``` #include <Fusion/Fusion/FusionProductPreferences.h>  // Get the value of the property. boolean propertyValue = fusionProductPreferences_var->isAutoProjectEdgesOnReference();  // Set the value of the property, where value_var is a boolean. bool returnValue = fusionProductPreferences_var->isAutoProjectEdgesOnReference(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |