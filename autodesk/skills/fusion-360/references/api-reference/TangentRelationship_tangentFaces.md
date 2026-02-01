# TangentRelationship.tangentFaces Property

Parent Object: [TangentRelationship](TangentRelationship.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/TangentRelationship.h>

## Description

Gets and sets a single BRepFace object that is part of the body that faceOne will remain tangent to. All of the faces of the body will be used when computing the tangent relationship.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tangentRelationship\_var" is a variable referencing a TangentRelationship object.  ```` ``` # Get the value of the property. propertyValue = tangentRelationship_var.tangentFaces  # Set the value of the property. tangentRelationship_var.tangentFaces = propertyValue ``` ```` |

"tangentRelationship\_var" is a variable referencing a TangentRelationship object. ```` ``` #include <Fusion/Components/TangentRelationship.h>  // Get the value of the property. Ptr<Base> propertyValue = tangentRelationship_var->tangentFaces();  // Set the value of the property, where value_var is a Base. bool returnValue = tangentRelationship_var->tangentFaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |