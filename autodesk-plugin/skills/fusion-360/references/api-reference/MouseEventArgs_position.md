# MouseEventArgs.position Property

Parent Object: [MouseEventArgs](MouseEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MouseEventArgs.h>

## Description

Gets the coordinate of the mouse in screen space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mouseEventArgs\_var" is a variable referencing a MouseEventArgs object. |

"mouseEventArgs\_var" is a variable referencing a MouseEventArgs object. ```` ``` #include <Core/UserInterface/MouseEventArgs.h>  // Get the value of the property. Ptr<Point2D> propertyValue = mouseEventArgs_var->position(); ``` ```` |

## Property Value

This is a read only property whose value is a [Point2D](Point2D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |