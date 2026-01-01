# ConstructionPlaneDefinition.objectType Property

Parent Object: [ConstructionPlaneDefinition](ConstructionPlaneDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneDefinition\_var" is a variable referencing a ConstructionPlaneDefinition object.  ```` ``` # Get the value of the property. propertyValue = constructionPlaneDefinition_var.objectType ``` ```` |

"constructionPlaneDefinition\_var" is a variable referencing a ConstructionPlaneDefinition object. ```` ``` #include <Fusion/Construction/ConstructionPlaneDefinition.h>  // Get the value of the property. string propertyValue = constructionPlaneDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |