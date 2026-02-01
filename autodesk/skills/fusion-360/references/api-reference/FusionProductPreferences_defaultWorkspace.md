# FusionProductPreferences.defaultWorkspace Property

Parent Object: [FusionProductPreferences](FusionProductPreferences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionProductPreferences.h>

## Description

Gets and sets the Default workspace setting. (Model, Sculpt or Patch)

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionProductPreferences\_var" is a variable referencing a FusionProductPreferences object. |

"fusionProductPreferences\_var" is a variable referencing a FusionProductPreferences object. ```` ``` #include <Fusion/Fusion/FusionProductPreferences.h>  // Get the value of the property. DefaultWorkspaces propertyValue = fusionProductPreferences_var->defaultWorkspace();  // Set the value of the property, where value_var is a DefaultWorkspaces. bool returnValue = fusionProductPreferences_var->defaultWorkspace(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [DefaultWorkspaces](DefaultWorkspaces.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |