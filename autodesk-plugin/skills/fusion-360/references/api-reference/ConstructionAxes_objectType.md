# ConstructionAxes.objectType Property

Parent Object: [ConstructionAxes](ConstructionAxes.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxes.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxes\_var" is a variable referencing a ConstructionAxes object.  ```` ``` # Get the value of the property. propertyValue = constructionAxes_var.objectType ``` ```` |

"constructionAxes\_var" is a variable referencing a ConstructionAxes object. ```` ``` #include <Fusion/Construction/ConstructionAxes.h>  // Get the value of the property. string propertyValue = constructionAxes_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |