# Arc2D.createByCenter Method

Parent Object: [Arc2D](Arc2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Arc2D.h>

## Description

Creates a transient 2D arc object specifying the center, radius and start and end angles. A transient arc is not displayed or saved in a document. Transient arcs are used as a wrapper to work with raw 2D arc information.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. ```` ```  #include <Core/Geometry/Arc2D.h> ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Arc2D](Arc2D.htm) | Returns the newly created arc or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| center | [Point2D](Point2D.htm) | A Point2D object that defines the center position of the arc in 2D space. |
| radius | double | The radius of the arc. |
| startAngle | double | The start angle in radians, where 0 is along the X-axis. |
| endAngle | double | The end angle in radians, where 0 is along the X-axis. |
| isClockwise | boolean | Specifies if the sweep of the arc is clockwise or counterclockwise from the start to end angle.   This is an optional argument whose default value is False. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |