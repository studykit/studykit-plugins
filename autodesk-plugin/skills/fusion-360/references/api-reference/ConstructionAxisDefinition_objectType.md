# ConstructionAxisDefinition.objectType Property

Parent Object: [ConstructionAxisDefinition](ConstructionAxisDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxisDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxisDefinition\_var" is a variable referencing a ConstructionAxisDefinition object.  ```` ``` # Get the value of the property. propertyValue = constructionAxisDefinition_var.objectType ``` ```` |

"constructionAxisDefinition\_var" is a variable referencing a ConstructionAxisDefinition object. ```` ``` #include <Fusion/Construction/ConstructionAxisDefinition.h>  // Get the value of the property. string propertyValue = constructionAxisDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |