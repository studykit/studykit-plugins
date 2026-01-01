# BRepLump.pointContainment Method

Parent Object: [BRepLump](BRepLump.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLump.h>

## Description

Determines the relationship of the input point with respect to this lump.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLump\_var" is a variable referencing a [BRepLump](BRepLump.htm) object.```` ``` returnValue = bRepLump_var.pointContainment(point) ``` ```` |

"bRepLump\_var" is a variable referencing a [BRepLump](BRepLump.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PointContainment](PointContainment.htm) | Returns a value from the PointContainment enum indicating the relationship of the input point to the lump. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| point | [Point3D](Point3D.htm) | The point to do the containment check for. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |