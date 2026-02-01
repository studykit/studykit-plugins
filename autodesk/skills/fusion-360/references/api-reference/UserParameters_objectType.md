# UserParameters.objectType Property

Parent Object: [UserParameters](UserParameters.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/UserParameters.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userParameters\_var" is a variable referencing a UserParameters object.  ```` ``` # Get the value of the property. propertyValue = userParameters_var.objectType ``` ```` |

"userParameters\_var" is a variable referencing a UserParameters object. ```` ``` #include <Fusion/Fusion/UserParameters.h>  // Get the value of the property. string propertyValue = userParameters_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |