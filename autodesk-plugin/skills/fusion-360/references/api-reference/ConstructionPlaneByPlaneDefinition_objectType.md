# ConstructionPlaneByPlaneDefinition.objectType Property

Parent Object: [ConstructionPlaneByPlaneDefinition](ConstructionPlaneByPlaneDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneByPlaneDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneByPlaneDefinition\_var" is a variable referencing a ConstructionPlaneByPlaneDefinition object.  ```` ``` # Get the value of the property. propertyValue = constructionPlaneByPlaneDefinition_var.objectType ``` ```` |

"constructionPlaneByPlaneDefinition\_var" is a variable referencing a ConstructionPlaneByPlaneDefinition object. ```` ``` #include <Fusion/Construction/ConstructionPlaneByPlaneDefinition.h>  // Get the value of the property. string propertyValue = constructionPlaneByPlaneDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |