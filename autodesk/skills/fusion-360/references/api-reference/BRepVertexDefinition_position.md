# BRepVertexDefinition.position Property

Parent Object: [BRepVertexDefinition](BRepVertexDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepVertexDefinition.h>

## Description

Gets and sets the position of the vertex in model space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepVertexDefinition\_var" is a variable referencing a BRepVertexDefinition object. |

"bRepVertexDefinition\_var" is a variable referencing a BRepVertexDefinition object. ```` ``` #include <Fusion/BRep/BRepVertexDefinition.h>  // Get the value of the property. Ptr<Point3D> propertyValue = bRepVertexDefinition_var->position();  // Set the value of the property, where value_var is a Point3D. bool returnValue = bRepVertexDefinition_var->position(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |