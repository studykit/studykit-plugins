# CopyPasteBodies.objectType Property

Parent Object: [CopyPasteBodies](CopyPasteBodies.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CopyPasteBodies.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"copyPasteBodies\_var" is a variable referencing a CopyPasteBodies object.  ```` ``` # Get the value of the property. propertyValue = copyPasteBodies_var.objectType ``` ```` |

"copyPasteBodies\_var" is a variable referencing a CopyPasteBodies object. ```` ``` #include <Fusion/Features/CopyPasteBodies.h>  // Get the value of the property. string propertyValue = copyPasteBodies_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |