# ConstructionPoint.objectType Property

Parent Object: [ConstructionPoint](ConstructionPoint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPoint.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPoint\_var" is a variable referencing a ConstructionPoint object.  ```` ``` # Get the value of the property. propertyValue = constructionPoint_var.objectType ``` ```` |

"constructionPoint\_var" is a variable referencing a ConstructionPoint object. ```` ``` #include <Fusion/Construction/ConstructionPoint.h>  // Get the value of the property. string propertyValue = constructionPoint_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |