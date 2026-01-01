# Cone.getData Method

Parent Object: [Cone](Cone.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Cone.h>

## Description

Gets the data that defines the cone.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cone\_var" is a variable referencing a [Cone](Cone.htm) object. |

```` ```  #include <Core/Geometry/Cone.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| origin | [Point3D](Point3D.htm) | The output origin point (center) of the base of the cone. |
| axis | [Vector3D](Vector3D.htm) | The output center axis (along the length) of the cone that defines its normal direction. |
| radius | double | The output radius of the cone. |
| halfAngle | double | The output taper half-angle of the cone. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |