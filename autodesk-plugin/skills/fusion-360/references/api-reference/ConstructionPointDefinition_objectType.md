# ConstructionPointDefinition.objectType Property

Parent Object: [ConstructionPointDefinition](ConstructionPointDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPointDefinition\_var" is a variable referencing a ConstructionPointDefinition object.  ```` ``` # Get the value of the property. propertyValue = constructionPointDefinition_var.objectType ``` ```` |

"constructionPointDefinition\_var" is a variable referencing a ConstructionPointDefinition object. ```` ``` #include <Fusion/Construction/ConstructionPointDefinition.h>  // Get the value of the property. string propertyValue = constructionPointDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |