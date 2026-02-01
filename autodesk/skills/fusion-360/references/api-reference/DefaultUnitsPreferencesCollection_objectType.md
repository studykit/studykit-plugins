# DefaultUnitsPreferencesCollection.objectType Property

Parent Object: [DefaultUnitsPreferencesCollection](DefaultUnitsPreferencesCollection.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DefaultUnitsPreferencesCollection.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"defaultUnitsPreferencesCollection\_var" is a variable referencing a DefaultUnitsPreferencesCollection object.  ```` ``` # Get the value of the property. propertyValue = defaultUnitsPreferencesCollection_var.objectType ``` ```` |

"defaultUnitsPreferencesCollection\_var" is a variable referencing a DefaultUnitsPreferencesCollection object. ```` ``` #include <Core/Application/DefaultUnitsPreferencesCollection.h>  // Get the value of the property. string propertyValue = defaultUnitsPreferencesCollection_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |