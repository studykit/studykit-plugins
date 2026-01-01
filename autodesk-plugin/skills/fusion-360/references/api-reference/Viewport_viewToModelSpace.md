# Viewport.viewToModelSpace Method

Parent Object: [Viewport](Viewport.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Viewport.h>

## Description

A specified point in view space returns the equivalent point in model space. Because view space is 2D and model space is 3D, the depth of the point is returned is somewhat arbitrary along the eye to target point direction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"viewport\_var" is a variable referencing a [Viewport](Viewport.htm) object.```` ``` returnValue = viewport_var.viewToModelSpace(viewCoordinate) ``` ```` |

"viewport\_var" is a variable referencing a [Viewport](Viewport.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Point3D](Point3D.htm) | Returns the equivalent point in model space. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| viewCoordinate | [Point2D](Point2D.htm) | A coordinate in view space. |

## Version

Introduced in version December 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |