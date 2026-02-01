# Viewport.viewToScreen Method

Parent Object: [Viewport](Viewport.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Viewport.h>

## Description

Converts a 2D viewPort point into the equivalent screen coordinate.

## Syntax

* [Python](#Python)
* [C++](#C++)

"viewport\_var" is a variable referencing a [Viewport](Viewport.htm) object.```` ``` returnValue = viewport_var.viewToScreen(viewCoordinate) ``` ```` |

"viewport\_var" is a variable referencing a [Viewport](Viewport.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Point2D](Point2D.htm) | Returns the equivalent point in the screen. This can return null in the case where the input point is outside the bounds of the screen, which also means it's outside any viewport. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| viewCoordinate | [Point2D](Point2D.htm) | A 2D coordinate in the viewport. (0,0) indicates the upper-left corner of the viewport. |

## Version

Introduced in version April 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |