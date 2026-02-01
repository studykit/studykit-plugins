# EllipticalCone.getAxes Method

Parent Object: [EllipticalCone](EllipticalCone.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalCone.h>

## Description

Gets the center axis of the cone that defines its normal direction and the major axis direction of the ellipse that defines it.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalCone\_var" is a variable referencing an [EllipticalCone](EllipticalCone.htm) object. |

```` ```  #include <Core/Geometry/EllipticalCone.h ``` ```` |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| axis | [Vector3D](Vector3D.htm) | The output center axis (along the length) of the cone that defines its normal direction. |
| majorAxisDirection | [Vector3D](Vector3D.htm) | The output direction of the major axis of the ellipse that defines the cone. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |