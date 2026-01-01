# Torus.getData Method

Parent Object: [Torus](Torus.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Torus.h>

## Description

Gets all of the data defining the torus.

## Syntax

* [Python](#Python)
* [C++](#C++)

"torus\_var" is a variable referencing a [Torus](Torus.htm) object. |

```` ```  #include <Core/Geometry/Torus.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| origin | [Point3D](Point3D.htm) | The output origin point (center) of the torus. |
| axis | [Vector3D](Vector3D.htm) | The output center axis of the torus. |
| majorRadius | double | The output major radius of the torus. |
| minorRadius | double | The output minor radius of the torus. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |