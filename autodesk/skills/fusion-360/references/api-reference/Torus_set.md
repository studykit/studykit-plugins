# Torus.set Method

Parent Object: [Torus](Torus.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Torus.h>

## Description

Sets all of the data defining the torus.

## Syntax

* [Python](#Python)
* [C++](#C++)

"torus\_var" is a variable referencing a [Torus](Torus.htm) object.```` ``` returnValue = torus_var.set(origin, axis, majorRadius, minorRadius) ``` ```` |

"torus\_var" is a variable referencing a [Torus](Torus.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| origin | [Point3D](Point3D.htm) | The origin point (center) of the torus. |
| axis | [Vector3D](Vector3D.htm) | The center axis of the torus. |
| majorRadius | double | The major radius of the torus. |
| minorRadius | double | The minor radius of the torus. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |