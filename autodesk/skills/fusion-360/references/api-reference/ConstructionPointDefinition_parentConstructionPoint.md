# ConstructionPointDefinition.parentConstructionPoint Property

Parent Object: [ConstructionPointDefinition](ConstructionPointDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointDefinition.h>

## Description

Returns the ConstructionPoint object

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPointDefinition\_var" is a variable referencing a ConstructionPointDefinition object. |

"constructionPointDefinition\_var" is a variable referencing a ConstructionPointDefinition object. ```` ``` #include <Fusion/Construction/ConstructionPointDefinition.h>  // Get the value of the property. Ptr<ConstructionPoint> propertyValue = constructionPointDefinition_var->parentConstructionPoint(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConstructionPoint](ConstructionPoint.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |