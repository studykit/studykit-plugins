# ConstructionPointPointDefinition.objectType Property

Parent Object: [ConstructionPointPointDefinition](ConstructionPointPointDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointPointDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPointPointDefinition\_var" is a variable referencing a ConstructionPointPointDefinition object.  ```` ``` # Get the value of the property. propertyValue = constructionPointPointDefinition_var.objectType ``` ```` |

"constructionPointPointDefinition\_var" is a variable referencing a ConstructionPointPointDefinition object. ```` ``` #include <Fusion/Construction/ConstructionPointPointDefinition.h>  // Get the value of the property. string propertyValue = constructionPointPointDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |