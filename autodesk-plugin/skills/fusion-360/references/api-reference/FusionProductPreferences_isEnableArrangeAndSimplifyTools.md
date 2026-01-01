# FusionProductPreferences.isEnableArrangeAndSimplifyTools Property

Parent Object: [FusionProductPreferences](FusionProductPreferences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionProductPreferences.h>

## Description

Gets and sets if the Arrange, Remove Features, Remove Faces, and Replace with Primitives commands should be added to the Modify menu in the Design workspace.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionProductPreferences\_var" is a variable referencing a FusionProductPreferences object. |

"fusionProductPreferences\_var" is a variable referencing a FusionProductPreferences object. ```` ``` #include <Fusion/Fusion/FusionProductPreferences.h>  // Get the value of the property. boolean propertyValue = fusionProductPreferences_var->isEnableArrangeAndSimplifyTools();  // Set the value of the property, where value_var is a boolean. bool returnValue = fusionProductPreferences_var->isEnableArrangeAndSimplifyTools(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |