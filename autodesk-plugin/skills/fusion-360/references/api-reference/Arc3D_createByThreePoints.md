# Arc3D.createByThreePoints Method

Parent Object: [Arc3D](Arc3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Arc3D.h>

## Description

Creates a transient 3D arc by specifying 3 points. A transient arc is not displayed or saved in a document. Transient arcs are used as a wrapper to work with raw 3D arc information.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Arc3D](Arc3D.htm) | Returns the newly created arc or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| pointOne | [Point3D](Point3D.htm) | The start point of the arc. |
| pointTwo | [Point3D](Point3D.htm) | A point along the arc. This point must not be coincident with the first or third points. This point must not lie on the line between the first and third points. |
| pointThree | [Point3D](Point3D.htm) | The end point of the arc. This point must not be coincident with the first or second points. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchFixedSplines.addByNurbsCurve](SketchFixedSplines_addByNurbsCurve_Sample.htm) | Demonstrates the SketchFixedSplines.addByNurbsCurve method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |