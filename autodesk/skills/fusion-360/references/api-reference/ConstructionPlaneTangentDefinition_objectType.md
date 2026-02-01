# ConstructionPlaneTangentDefinition.objectType Property

Parent Object: [ConstructionPlaneTangentDefinition](ConstructionPlaneTangentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneTangentDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneTangentDefinition\_var" is a variable referencing a ConstructionPlaneTangentDefinition object.  ```` ``` # Get the value of the property. propertyValue = constructionPlaneTangentDefinition_var.objectType ``` ```` |

"constructionPlaneTangentDefinition\_var" is a variable referencing a ConstructionPlaneTangentDefinition object. ```` ``` #include <Fusion/Construction/ConstructionPlaneTangentDefinition.h>  // Get the value of the property. string propertyValue = constructionPlaneTangentDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |