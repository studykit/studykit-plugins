# BRepEdgeDefinition.modelSpaceCurve Property

Parent Object: [BRepEdgeDefinition](BRepEdgeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepEdgeDefinition.h>

## Description

Gets and sets the curve that defines the shape of the edge.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepEdgeDefinition\_var" is a variable referencing a BRepEdgeDefinition object. |

"bRepEdgeDefinition\_var" is a variable referencing a BRepEdgeDefinition object. ```` ``` #include <Fusion/BRep/BRepEdgeDefinition.h>  // Get the value of the property. Ptr<Curve3D> propertyValue = bRepEdgeDefinition_var->modelSpaceCurve();  // Set the value of the property, where value_var is a Curve3D. bool returnValue = bRepEdgeDefinition_var->modelSpaceCurve(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Curve3D](Curve3D.htm).

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |