# ConstructionPlaneByPlaneDefinition.plane Property

Parent Object: [ConstructionPlaneByPlaneDefinition](ConstructionPlaneByPlaneDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneByPlaneDefinition.h>

## Description

Gets and sets the position of the construction plane. Setting this property is only valid for a construction plane in a direct edit design or in a base feature. Construction planes in a parametric model are parametrically controlled and cannot be directly edited.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneByPlaneDefinition\_var" is a variable referencing a ConstructionPlaneByPlaneDefinition object. |

"constructionPlaneByPlaneDefinition\_var" is a variable referencing a ConstructionPlaneByPlaneDefinition object. ```` ``` #include <Fusion/Construction/ConstructionPlaneByPlaneDefinition.h>  // Get the value of the property. Ptr<Plane> propertyValue = constructionPlaneByPlaneDefinition_var->plane();  // Set the value of the property, where value_var is a Plane. bool returnValue = constructionPlaneByPlaneDefinition_var->plane(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Plane](Plane.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |