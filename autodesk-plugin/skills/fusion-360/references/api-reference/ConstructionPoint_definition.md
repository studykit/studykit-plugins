# ConstructionPoint.definition Property

Parent Object: [ConstructionPoint](ConstructionPoint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPoint.h>

## Description

Returns the construction point definition object which provides access to the information defining the construction point.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPoint\_var" is a variable referencing a ConstructionPoint object. |

"constructionPoint\_var" is a variable referencing a ConstructionPoint object. ```` ``` #include <Fusion/Construction/ConstructionPoint.h>  // Get the value of the property. Ptr<ConstructionPointDefinition> propertyValue = constructionPoint_var->definition(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConstructionPointDefinition](ConstructionPointDefinition.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |