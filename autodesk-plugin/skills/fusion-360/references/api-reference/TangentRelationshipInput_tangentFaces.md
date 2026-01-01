# TangentRelationshipInput.tangentFaces Property

Parent Object: [TangentRelationshipInput](TangentRelationshipInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/TangentRelationshipInput.h>

## Description

Gets and sets a single BRepFace object that is part of the body that faceOne will remain tangent to. All of the faces of the body will be used when computing the tangent relationship.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tangentRelationshipInput\_var" is a variable referencing a TangentRelationshipInput object. |

"tangentRelationshipInput\_var" is a variable referencing a TangentRelationshipInput object. ```` ``` #include <Fusion/Components/TangentRelationshipInput.h>  // Get the value of the property. Ptr<Base> propertyValue = tangentRelationshipInput_var->tangentFaces();  // Set the value of the property, where value_var is a Base. bool returnValue = tangentRelationshipInput_var->tangentFaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |