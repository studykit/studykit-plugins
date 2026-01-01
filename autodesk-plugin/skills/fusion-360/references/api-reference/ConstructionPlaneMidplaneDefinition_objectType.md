# ConstructionPlaneMidplaneDefinition.objectType Property

Parent Object: [ConstructionPlaneMidplaneDefinition](ConstructionPlaneMidplaneDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneMidplaneDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneMidplaneDefinition\_var" is a variable referencing a ConstructionPlaneMidplaneDefinition object.  ```` ``` # Get the value of the property. propertyValue = constructionPlaneMidplaneDefinition_var.objectType ``` ```` |

"constructionPlaneMidplaneDefinition\_var" is a variable referencing a ConstructionPlaneMidplaneDefinition object. ```` ``` #include <Fusion/Construction/ConstructionPlaneMidplaneDefinition.h>  // Get the value of the property. string propertyValue = constructionPlaneMidplaneDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |