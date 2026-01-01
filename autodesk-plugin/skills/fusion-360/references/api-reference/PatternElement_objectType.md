# PatternElement.objectType Property

Parent Object: [PatternElement](PatternElement.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatternElement.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patternElement\_var" is a variable referencing a PatternElement object.  ```` ``` # Get the value of the property. propertyValue = patternElement_var.objectType ``` ```` |

"patternElement\_var" is a variable referencing a PatternElement object. ```` ``` #include <Fusion/Features/PatternElement.h>  // Get the value of the property. string propertyValue = patternElement_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |