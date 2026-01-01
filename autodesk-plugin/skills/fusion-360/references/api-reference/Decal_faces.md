# Decal.faces Property

Parent Object: [Decal](Decal.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Decal.h>

## Description

Gets the faces the decal is associated with. Typically, this is an array containing a single face. If the isChainFaces property is true, this will return the primary face. If the isChainFaces property is false, the decal is limited to the faces in this list.

## Syntax

* [Python](#Python)
* [C++](#C++)

"decal\_var" is a variable referencing a Decal object.  ```` ``` # Get the value of the property. propertyValue = decal_var.faces ``` ```` |

"decal\_var" is a variable referencing a Decal object. ```` ``` #include <Fusion/Image/Decal.h>  // Get the value of the property. std::vector<Ptr<BRepFace>> propertyValue = decal_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [BRepFace](BRepFace.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |