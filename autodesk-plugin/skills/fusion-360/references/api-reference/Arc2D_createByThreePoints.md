# Arc2D.createByThreePoints Method

Parent Object: [Arc2D](Arc2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Arc2D.h>

## Description

Creates a transient 2D arc by specifying 3 points. A transient arc is not displayed or saved in a document. Transient arcs are used as a wrapper to work with raw 2D arc information.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Arc2D](Arc2D.htm) | Returns the newly created arc or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| startPoint | [Point2D](Point2D.htm) | The start point of the arc. |
| point | [Point2D](Point2D.htm) | A point along the arc. |
| endPoint | [Point2D](Point2D.htm) | The end point of the arc. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |