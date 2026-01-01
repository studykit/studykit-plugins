# Plane.isPerpendicularToLine Method

Parent Object: [Plane](Plane.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Plane.h>

## Description

Checks if this plane is perpendicular to a line.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plane\_var" is a variable referencing a [Plane](Plane.htm) object.```` ``` returnValue = plane_var.isPerpendicularToLine(line) ``` ```` |

"plane\_var" is a variable referencing a [Plane](Plane.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the plane and line are perpendicular. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| line | [Line3D](Line3D.htm) | The line to compare with for perpendicularity. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |