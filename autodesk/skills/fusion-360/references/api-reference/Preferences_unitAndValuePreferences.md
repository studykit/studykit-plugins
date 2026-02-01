# Preferences.unitAndValuePreferences Property

Parent Object: [Preferences](Preferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Preferences.h>

## Description

Gets the UnitAndValuePreferences object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"preferences\_var" is a variable referencing a Preferences object. |

"preferences\_var" is a variable referencing a Preferences object. ```` ``` #include <Core/Application/Preferences.h>  // Get the value of the property. Ptr<UnitAndValuePreferences> propertyValue = preferences_var->unitAndValuePreferences(); ``` ```` |

## Property Value

This is a read only property whose value is a [UnitAndValuePreferences](UnitAndValuePreferences.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |