# BRepWireEdgeDefinition.modelSpaceCurve Property

Parent Object: [BRepWireEdgeDefinition](BRepWireEdgeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWireEdgeDefinition.h>

## Description

Gets and sets the Curve3D object that defines the shape of the edge using 3D geometry in model space. Valid objects are an Arc3D, NurbsCurve3D, Circle3D, Ellipse3D, EllipticalArc3D, or Line3D.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepWireEdgeDefinition\_var" is a variable referencing a BRepWireEdgeDefinition object. |

"bRepWireEdgeDefinition\_var" is a variable referencing a BRepWireEdgeDefinition object. ```` ``` #include <Fusion/BRep/BRepWireEdgeDefinition.h>  // Get the value of the property. Ptr<Curve3D> propertyValue = bRepWireEdgeDefinition_var->modelSpaceCurve();  // Set the value of the property, where value_var is a Curve3D. bool returnValue = bRepWireEdgeDefinition_var->modelSpaceCurve(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Curve3D](Curve3D.htm).

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |