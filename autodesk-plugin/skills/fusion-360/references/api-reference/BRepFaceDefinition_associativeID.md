# BRepFaceDefinition.associativeID Property

Parent Object: [BRepFaceDefinition](BRepFaceDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepFaceDefinition.h>

## Description

Gets and sets the associate ID of this face definition. This ID will be copied to the corresponding face when the BRepBodyDefinition is used to create a BrepBody. It is used by Fusion as the identifier for the face and is used for tracking this geometry for parametric recomputes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepFaceDefinition\_var" is a variable referencing a BRepFaceDefinition object. |

"bRepFaceDefinition\_var" is a variable referencing a BRepFaceDefinition object. ```` ``` #include <Fusion/BRep/BRepFaceDefinition.h>  // Get the value of the property. integer propertyValue = bRepFaceDefinition_var->associativeID();  // Set the value of the property, where value_var is an integer. bool returnValue = bRepFaceDefinition_var->associativeID(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |