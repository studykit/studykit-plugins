# ConstructionPointCenterDefinition.circularEntity Property

Parent Object: [ConstructionPointCenterDefinition](ConstructionPointCenterDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointCenterDefinition.h>

## Description

Gets and sets the spherical face (sphere or torus), circular edge or sketch arc/circle whose center defines the location for the construction point.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPointCenterDefinition\_var" is a variable referencing a ConstructionPointCenterDefinition object. |

"constructionPointCenterDefinition\_var" is a variable referencing a ConstructionPointCenterDefinition object. ```` ``` #include <Fusion/Construction/ConstructionPointCenterDefinition.h>  // Get the value of the property. Ptr<Base> propertyValue = constructionPointCenterDefinition_var->circularEntity();  // Set the value of the property, where value_var is a Base. bool returnValue = constructionPointCenterDefinition_var->circularEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |