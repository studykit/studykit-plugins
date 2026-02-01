# BRepFaceDefinitions.add Method

Parent Object: [BRepFaceDefinitions](BRepFaceDefinitions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepFaceDefinitions.h>

## Description

Creates a new BrepFaceDefinition within the parent BRepShellDefinition object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepFaceDefinitions\_var" is a variable referencing a [BRepFaceDefinitions](BRepFaceDefinitions.htm) object.```` ``` returnValue = bRepFaceDefinitions_var.add(surfaceGeometry, isParamReversed) ``` ```` |

"bRepFaceDefinitions\_var" is a variable referencing a [BRepFaceDefinitions](BRepFaceDefinitions.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepFaceDefinition](BRepFaceDefinition.htm) | Returns the newly created BRepFaceDefinition object or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| surfaceGeometry | [Surface](Surface.htm) | Input surface object that defines the geometry of the face. Valid objects for input are NurbsSurface, Cone, Cylinder, EllipticalCone, EllipticalCylinder, Plane, Sphere, and Torus. |
| isParamReversed | boolean | Input Boolean that indicates if the normal of this face is reversed with respect to the surface geometry associated with this face definition. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BRep Body definition Sample](BRepBodyDefinition_Sample.htm) | Demonstrates creating BRep bodies by BRepBodyDefinition. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |