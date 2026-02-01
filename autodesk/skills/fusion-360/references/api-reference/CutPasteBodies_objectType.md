# CutPasteBodies.objectType Property

Parent Object: [CutPasteBodies](CutPasteBodies.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CutPasteBodies.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cutPasteBodies\_var" is a variable referencing a CutPasteBodies object.  ```` ``` # Get the value of the property. propertyValue = cutPasteBodies_var.objectType ``` ```` |

"cutPasteBodies\_var" is a variable referencing a CutPasteBodies object. ```` ``` #include <Fusion/Features/CutPasteBodies.h>  // Get the value of the property. string propertyValue = cutPasteBodies_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |