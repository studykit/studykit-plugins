# TangentRelationship.faceOne Property

Parent Object: [TangentRelationship](TangentRelationship.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/TangentRelationship.h>

## Description

Gets and sets the first BRepFace object that will remain tangent to the set of specified tangent faces.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tangentRelationship\_var" is a variable referencing a TangentRelationship object.  ```` ``` # Get the value of the property. propertyValue = tangentRelationship_var.faceOne  # Set the value of the property. tangentRelationship_var.faceOne = propertyValue ``` ```` |

"tangentRelationship\_var" is a variable referencing a TangentRelationship object. ```` ``` #include <Fusion/Components/TangentRelationship.h>  // Get the value of the property. Ptr<Base> propertyValue = tangentRelationship_var->faceOne();  // Set the value of the property, where value_var is a Base. bool returnValue = tangentRelationship_var->faceOne(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |