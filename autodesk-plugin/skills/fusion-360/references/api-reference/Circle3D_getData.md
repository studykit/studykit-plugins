# Circle3D.getData Method

Parent Object: [Circle3D](Circle3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Circle3D.h>

## Description

Gets all of the data defining the circle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circle3D\_var" is a variable referencing a [Circle3D](Circle3D.htm) object. |

```` ```  #include <Core/Geometry/Circle3D.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| center | [Point3D](Point3D.htm) | The output center point of the circle. |
| normal | [Vector3D](Vector3D.htm) | The output normal vector. |
| radius | double | The output radius of the circle. |

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