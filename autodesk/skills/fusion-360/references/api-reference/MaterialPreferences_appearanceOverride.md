# MaterialPreferences.appearanceOverride Property

Parent Object: [MaterialPreferences](MaterialPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/MaterialPreferences.h>

## Description

Gets and sets an appearance override. This property return null indicating that there is no override, or be set to null to remove the current appearance override.

## Syntax

* [Python](#Python)
* [C++](#C++)

"materialPreferences\_var" is a variable referencing a MaterialPreferences object. |

"materialPreferences\_var" is a variable referencing a MaterialPreferences object. ```` ``` #include <Core/Application/MaterialPreferences.h>  // Get the value of the property. Ptr<Appearance> propertyValue = materialPreferences_var->appearanceOverride();  // Set the value of the property, where value_var is an Appearance. bool returnValue = materialPreferences_var->appearanceOverride(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [Appearance](Appearance.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |