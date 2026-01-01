# ConstructionAxisCircularFaceDefinition.circularFace Property

Parent Object: [ConstructionAxisCircularFaceDefinition](ConstructionAxisCircularFaceDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxisCircularFaceDefinition.h>

## Description

Gets and sets the cylinder, cone, or torus this work axis is parametrically dependent on.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxisCircularFaceDefinition\_var" is a variable referencing a ConstructionAxisCircularFaceDefinition object. |

"constructionAxisCircularFaceDefinition\_var" is a variable referencing a ConstructionAxisCircularFaceDefinition object. ```` ``` #include <Fusion/Construction/ConstructionAxisCircularFaceDefinition.h>  // Get the value of the property. Ptr<BRepFace> propertyValue = constructionAxisCircularFaceDefinition_var->circularFace();  // Set the value of the property, where value_var is a BRepFace. bool returnValue = constructionAxisCircularFaceDefinition_var->circularFace(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BRepFace](BRepFace.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |