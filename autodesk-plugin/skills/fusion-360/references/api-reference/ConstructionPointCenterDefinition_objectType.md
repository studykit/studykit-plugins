# ConstructionPointCenterDefinition.objectType Property

Parent Object: [ConstructionPointCenterDefinition](ConstructionPointCenterDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointCenterDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPointCenterDefinition\_var" is a variable referencing a ConstructionPointCenterDefinition object.  ```` ``` # Get the value of the property. propertyValue = constructionPointCenterDefinition_var.objectType ``` ```` |

"constructionPointCenterDefinition\_var" is a variable referencing a ConstructionPointCenterDefinition object. ```` ``` #include <Fusion/Construction/ConstructionPointCenterDefinition.h>  // Get the value of the property. string propertyValue = constructionPointCenterDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |