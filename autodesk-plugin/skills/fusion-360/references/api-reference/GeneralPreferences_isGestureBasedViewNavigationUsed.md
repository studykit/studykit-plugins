# GeneralPreferences.isGestureBasedViewNavigationUsed Property

Parent Object: [GeneralPreferences](GeneralPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/GeneralPreferences.h>

## Description

Gets and sets if gesture based view navigation is used.

## Syntax

* [Python](#Python)
* [C++](#C++)

"generalPreferences\_var" is a variable referencing a GeneralPreferences object. |

"generalPreferences\_var" is a variable referencing a GeneralPreferences object. ```` ``` #include <Core/Application/GeneralPreferences.h>  // Get the value of the property. boolean propertyValue = generalPreferences_var->isGestureBasedViewNavigationUsed();  // Set the value of the property, where value_var is a boolean. bool returnValue = generalPreferences_var->isGestureBasedViewNavigationUsed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |