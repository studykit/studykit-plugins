# ConstructionPoints.objectType Property

Parent Object: [ConstructionPoints](ConstructionPoints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPoints.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPoints\_var" is a variable referencing a ConstructionPoints object.  ```` ``` # Get the value of the property. propertyValue = constructionPoints_var.objectType ``` ```` |

"constructionPoints\_var" is a variable referencing a ConstructionPoints object. ```` ``` #include <Fusion/Construction/ConstructionPoints.h>  // Get the value of the property. string propertyValue = constructionPoints_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |