# FusionProductPreferences.isAllowReferencesDuringEditInPlace Property

Parent Object: [FusionProductPreferences](FusionProductPreferences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionProductPreferences.h>

## Description

Gets and sets if you can create associative references while editing external components in context.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionProductPreferences\_var" is a variable referencing a FusionProductPreferences object. |

"fusionProductPreferences\_var" is a variable referencing a FusionProductPreferences object. ```` ``` #include <Fusion/Fusion/FusionProductPreferences.h>  // Get the value of the property. boolean propertyValue = fusionProductPreferences_var->isAllowReferencesDuringEditInPlace();  // Set the value of the property, where value_var is a boolean. bool returnValue = fusionProductPreferences_var->isAllowReferencesDuringEditInPlace(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |