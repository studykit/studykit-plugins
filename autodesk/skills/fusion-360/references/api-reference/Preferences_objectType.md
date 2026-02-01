# Preferences.objectType Property

Parent Object: [Preferences](Preferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Preferences.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"preferences\_var" is a variable referencing a Preferences object.  ```` ``` # Get the value of the property. propertyValue = preferences_var.objectType ``` ```` |

"preferences\_var" is a variable referencing a Preferences object. ```` ``` #include <Core/Application/Preferences.h>  // Get the value of the property. string propertyValue = preferences_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |