# ConstructionPointPointDefinition.pointEntity Property

Parent Object: [ConstructionPointPointDefinition](ConstructionPointPointDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointPointDefinition.h>

## Description

Gets and sets the position of the point using a construction point, sketch point or vertex. Non-parametric points will always return a Point3D object

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPointPointDefinition\_var" is a variable referencing a ConstructionPointPointDefinition object. |

"constructionPointPointDefinition\_var" is a variable referencing a ConstructionPointPointDefinition object. ```` ``` #include <Fusion/Construction/ConstructionPointPointDefinition.h>  // Get the value of the property. Ptr<Base> propertyValue = constructionPointPointDefinition_var->pointEntity();  // Set the value of the property, where value_var is a Base. bool returnValue = constructionPointPointDefinition_var->pointEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |