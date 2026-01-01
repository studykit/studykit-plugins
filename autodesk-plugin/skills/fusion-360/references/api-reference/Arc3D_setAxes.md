# Arc3D.setAxes Method

Parent Object: [Arc3D](Arc3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Arc3D.h>

## Description

Sets the normal and reference vectors of the arc.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arc3D\_var" is a variable referencing an [Arc3D](Arc3D.htm) object.```` ``` returnValue = arc3D_var.setAxes(normal, referenceVector) ``` ```` |

"arc3D\_var" is a variable referencing an [Arc3D](Arc3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| normal | [Vector3D](Vector3D.htm) | The new normal vector. |
| referenceVector | [Vector3D](Vector3D.htm) | The new reference vector from which the start and end angles are measured from. The reference vector must be perpendicular to the normal vector. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |