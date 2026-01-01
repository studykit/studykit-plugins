# BRepFaceDefinition.surfaceGeometry Property

Parent Object: [BRepFaceDefinition](BRepFaceDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepFaceDefinition.h>

## Description

Gets and sets the surface geometry associated with this face definition.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepFaceDefinition\_var" is a variable referencing a BRepFaceDefinition object. |

"bRepFaceDefinition\_var" is a variable referencing a BRepFaceDefinition object. ```` ``` #include <Fusion/BRep/BRepFaceDefinition.h>  // Get the value of the property. Ptr<Surface> propertyValue = bRepFaceDefinition_var->surfaceGeometry();  // Set the value of the property, where value_var is a Surface. bool returnValue = bRepFaceDefinition_var->surfaceGeometry(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Surface](Surface.htm).

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |