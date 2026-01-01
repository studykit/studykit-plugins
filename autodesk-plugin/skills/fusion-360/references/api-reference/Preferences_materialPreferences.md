# Preferences.materialPreferences Property

Parent Object: [Preferences](Preferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Preferences.h>

## Description

Gets the MaterialPreferences object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"preferences\_var" is a variable referencing a Preferences object. |

"preferences\_var" is a variable referencing a Preferences object. ```` ``` #include <Core/Application/Preferences.h>  // Get the value of the property. Ptr<MaterialPreferences> propertyValue = preferences_var->materialPreferences(); ``` ```` |

## Property Value

This is a read only property whose value is a [MaterialPreferences](MaterialPreferences.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |