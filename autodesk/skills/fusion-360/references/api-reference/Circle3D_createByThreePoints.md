# Circle3D.createByThreePoints Method

Parent Object: [Circle3D](Circle3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Circle3D.h>

## Description

Creates a transient 3D circle through three points.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Circle3D](Circle3D.htm) | Returns the new Circle3D object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| pointOne | [Point3D](Point3D.htm) | The first point on the circle. |
| pointTwo | [Point3D](Point3D.htm) | The second point on the circle. This point cannot be coincident with pointOne or pointThree. This point cannot lie on the line defined by pointOne and pointThree. |
| pointThree | [Point3D](Point3D.htm) | The third point on the circle. This point cannot be coincident with pointOne or pointThree. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |