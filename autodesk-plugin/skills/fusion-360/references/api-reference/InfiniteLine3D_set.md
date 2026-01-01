# InfiniteLine3D.set Method

Parent Object: [InfiniteLine3D](InfiniteLine3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/InfiniteLine3D.h>

## Description

Sets all of the data defining the infinite line.

## Syntax

* [Python](#Python)
* [C++](#C++)

"infiniteLine3D\_var" is a variable referencing an [InfiniteLine3D](InfiniteLine3D.htm) object.```` ``` returnValue = infiniteLine3D_var.set(origin, direction) ``` ```` |

"infiniteLine3D\_var" is a variable referencing an [InfiniteLine3D](InfiniteLine3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| origin | [Point3D](Point3D.htm) | The origin point of the line. |
| direction | [Vector3D](Vector3D.htm) | The direction of the line. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |