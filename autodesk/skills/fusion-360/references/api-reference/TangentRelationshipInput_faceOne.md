# TangentRelationshipInput.faceOne Property

Parent Object: [TangentRelationshipInput](TangentRelationshipInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/TangentRelationshipInput.h>

## Description

Gets and sets the first BRepFace object that will remain tangent to the set of specified tangent faces.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tangentRelationshipInput\_var" is a variable referencing a TangentRelationshipInput object. |

"tangentRelationshipInput\_var" is a variable referencing a TangentRelationshipInput object. ```` ``` #include <Fusion/Components/TangentRelationshipInput.h>  // Get the value of the property. Ptr<BRepFace> propertyValue = tangentRelationshipInput_var->faceOne();  // Set the value of the property, where value_var is a BRepFace. bool returnValue = tangentRelationshipInput_var->faceOne(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BRepFace](BRepFace.htm).

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |