# ConstructionAxisEdgeDefinition.objectType Property

Parent Object: [ConstructionAxisEdgeDefinition](ConstructionAxisEdgeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxisEdgeDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxisEdgeDefinition\_var" is a variable referencing a ConstructionAxisEdgeDefinition object.  ```` ``` # Get the value of the property. propertyValue = constructionAxisEdgeDefinition_var.objectType ``` ```` |

"constructionAxisEdgeDefinition\_var" is a variable referencing a ConstructionAxisEdgeDefinition object. ```` ``` #include <Fusion/Construction/ConstructionAxisEdgeDefinition.h>  // Get the value of the property. string propertyValue = constructionAxisEdgeDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |