# Profiles.objectType Property

Parent Object: [Profiles](Profiles.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Profiles.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profiles\_var" is a variable referencing a Profiles object.  ```` ``` # Get the value of the property. propertyValue = profiles_var.objectType ``` ```` |

"profiles\_var" is a variable referencing a Profiles object. ```` ``` #include <Fusion/Sketch/Profiles.h>  // Get the value of the property. string propertyValue = profiles_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |