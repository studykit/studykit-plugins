# ConstructionPointEdgePlaneDefinition.objectType Property

Parent Object: [ConstructionPointEdgePlaneDefinition](ConstructionPointEdgePlaneDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointEdgePlaneDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPointEdgePlaneDefinition\_var" is a variable referencing a ConstructionPointEdgePlaneDefinition object.  ```` ``` # Get the value of the property. propertyValue = constructionPointEdgePlaneDefinition_var.objectType ``` ```` |

"constructionPointEdgePlaneDefinition\_var" is a variable referencing a ConstructionPointEdgePlaneDefinition object. ```` ``` #include <Fusion/Construction/ConstructionPointEdgePlaneDefinition.h>  // Get the value of the property. string propertyValue = constructionPointEdgePlaneDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |