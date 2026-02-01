# Preferences.apiPreferences Property

Parent Object: [Preferences](Preferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Preferences.h>

## Description

Gets the APIPreferences object, which provides access to the various preferences associated with the API.

## Syntax

* [Python](#Python)
* [C++](#C++)

"preferences\_var" is a variable referencing a Preferences object. |

"preferences\_var" is a variable referencing a Preferences object. ```` ``` #include <Core/Application/Preferences.h>  // Get the value of the property. Ptr<APIPreferences> propertyValue = preferences_var->apiPreferences(); ``` ```` |

## Property Value

This is a read only property whose value is an [APIPreferences](APIPreferences.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |