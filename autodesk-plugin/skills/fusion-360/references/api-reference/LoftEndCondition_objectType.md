# LoftEndCondition.objectType Property

Parent Object: [LoftEndCondition](LoftEndCondition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftEndCondition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftEndCondition\_var" is a variable referencing a LoftEndCondition object.  ```` ``` # Get the value of the property. propertyValue = loftEndCondition_var.objectType ``` ```` |

"loftEndCondition\_var" is a variable referencing a LoftEndCondition object. ```` ``` #include <Fusion/Features/LoftEndCondition.h>  // Get the value of the property. string propertyValue = loftEndCondition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |