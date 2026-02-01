# Arc2D.getData Method

Parent Object: [Arc2D](Arc2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Arc2D.h>

## Description

Gets all of the data defining the arc.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arc2D\_var" is a variable referencing an [Arc2D](Arc2D.htm) object. |

```` ```  #include <Core/Geometry/Arc2D.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| center | [Point2D](Point2D.htm) | The output center point of the arc. |
| radius | double | The output radius of the arc. |
| startAngle | double | The output start angle of the arc in radians, where 0 is along the x axis. |
| endAngle | double | The output end angle of the arc in radians, where 0 is along the x axis. |
| isClockwise | boolean | The output value that indicates if the sweep direction is clockwise or counterclockwise. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |