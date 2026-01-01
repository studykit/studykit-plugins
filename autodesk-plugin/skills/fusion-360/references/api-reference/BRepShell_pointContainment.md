# BRepShell.pointContainment Method

Parent Object: [BRepShell](BRepShell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepShell.h>

## Description

Determines the relationship of the input point with respect to this shell.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepShell\_var" is a variable referencing a [BRepShell](BRepShell.htm) object.```` ``` returnValue = bRepShell_var.pointContainment(point) ``` ```` |

"bRepShell\_var" is a variable referencing a [BRepShell](BRepShell.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PointContainment](PointContainment.htm) | Returns a value from the PointContainment enum indicating the relationship of the input point to the shell. |

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