# ConstructionAxisEdgeDefinition.edgeEntity Property

Parent Object: [ConstructionAxisEdgeDefinition](ConstructionAxisEdgeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxisEdgeDefinition.h>

## Description

Gets and sets the linear edge, construction line, or sketch line that defines the construction axis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxisEdgeDefinition\_var" is a variable referencing a ConstructionAxisEdgeDefinition object. |

"constructionAxisEdgeDefinition\_var" is a variable referencing a ConstructionAxisEdgeDefinition object. ```` ``` #include <Fusion/Construction/ConstructionAxisEdgeDefinition.h>  // Get the value of the property. Ptr<Base> propertyValue = constructionAxisEdgeDefinition_var->edgeEntity();  // Set the value of the property, where value_var is a Base. bool returnValue = constructionAxisEdgeDefinition_var->edgeEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |