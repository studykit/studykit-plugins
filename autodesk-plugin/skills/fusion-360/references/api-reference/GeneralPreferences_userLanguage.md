# GeneralPreferences.userLanguage Property

Parent Object: [GeneralPreferences](GeneralPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/GeneralPreferences.h>

## Description

Gets and sets the current language. Setting the language does not take effect until the next time Fusion is started.

## Syntax

* [Python](#Python)
* [C++](#C++)

"generalPreferences\_var" is a variable referencing a GeneralPreferences object. |

"generalPreferences\_var" is a variable referencing a GeneralPreferences object. ```` ``` #include <Core/Application/GeneralPreferences.h>  // Get the value of the property. UserLanguages propertyValue = generalPreferences_var->userLanguage();  // Set the value of the property, where value_var is a UserLanguages. bool returnValue = generalPreferences_var->userLanguage(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [UserLanguages](UserLanguages.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |