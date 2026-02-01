# DecalInput.faces Property

Parent Object: [DecalInput](DecalInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/DecalInput.h>

## Description

Gets and sets the faces the decal will be associated with. Typically, this will be an array containing a single face and the isChainFaces property on the input will be true. The position and orientation of the decal is based on this face and the decal can wrap onto other faces in the body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"decalInput\_var" is a variable referencing a DecalInput object.  ```` ``` # Get the value of the property. propertyValue = decalInput_var.faces  # Set the value of the property. decalInput_var.faces = propertyValue ``` ```` |

"decalInput\_var" is a variable referencing a DecalInput object. ```` ``` #include <Fusion/Image/DecalInput.h>  // Get the value of the property. std::vector<Ptr<BRepFace>> propertyValue = decalInput_var->faces();  // Set the value of the property, where value_var is a BRepFace. bool returnValue = decalInput_var->faces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [BRepFace](BRepFace.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |