# GeneralPreferences.userInterfaceTheme Property

Parent Object: [GeneralPreferences](GeneralPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/GeneralPreferences.h>

## Description

Gets and sets which color theme is used by the user interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"generalPreferences\_var" is a variable referencing a GeneralPreferences object. |

"generalPreferences\_var" is a variable referencing a GeneralPreferences object. ```` ``` #include <Core/Application/GeneralPreferences.h>  // Get the value of the property. UserInterfaceThemes propertyValue = generalPreferences_var->userInterfaceTheme();  // Set the value of the property, where value_var is a UserInterfaceThemes. bool returnValue = generalPreferences_var->userInterfaceTheme(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [UserInterfaceThemes](UserInterfaceThemes.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |