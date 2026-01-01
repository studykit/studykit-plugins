# Viewport.screenToView Method

Parent Object: [Viewport](Viewport.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Viewport.h>

## Description

Converts a 2D screen point into the equivalent viewport coordinate.

## Syntax

* [Python](#Python)
* [C++](#C++)

"viewport\_var" is a variable referencing a [Viewport](Viewport.htm) object.```` ``` returnValue = viewport_var.screenToView(screenCoordinate) ``` ```` |

"viewport\_var" is a variable referencing a [Viewport](Viewport.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Point2D](Point2D.htm) | Returns the equivalent point in the viewport. This can return null in the case where the input screen point does not lie within the viewport. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| screenCoordinate | [Point2D](Point2D.htm) | A 2D coordinate in screen space. (0,0) indicates the upper-left corner of the entire screen. |

## Version

Introduced in version April 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |