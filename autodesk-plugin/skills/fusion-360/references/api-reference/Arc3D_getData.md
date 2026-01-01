# Arc3D.getData Method

Parent Object: [Arc3D](Arc3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Arc3D.h>

## Description

Gets all of the data defining the arc.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arc3D\_var" is a variable referencing an [Arc3D](Arc3D.htm) object. |

```` ```  #include <Core/Geometry/Arc3D.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| center | [Point3D](Point3D.htm) | The output center point of the arc. |
| normal | [Vector3D](Vector3D.htm) | The output normal vector. |
| referenceVector | [Vector3D](Vector3D.htm) | The output reference vector. |
| radius | double | The output radius of the arc. |
| startAngle | double | The output start angle in radians. This angle is measured from the reference vector using the right hand rule around the normal vector. |
| endAngle | double | The output end angle in radians. This angle is measured from the reference vector using the right hand rule around the normal vector. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Get Circle and Arc Data from Edge API Sample](GetCircleAndArcDataFromEdge_Sample.htm) | Display the arc and circle geometric information from a selected circular edge. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |