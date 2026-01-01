# PatternElements.objectType Property

Parent Object: [PatternElements](PatternElements.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatternElements.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patternElements\_var" is a variable referencing a PatternElements object.  ```` ``` # Get the value of the property. propertyValue = patternElements_var.objectType ``` ```` |

"patternElements\_var" is a variable referencing a PatternElements object. ```` ``` #include <Fusion/Features/PatternElements.h>  // Get the value of the property. string propertyValue = patternElements_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |