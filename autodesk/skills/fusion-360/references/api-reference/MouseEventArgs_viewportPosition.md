# MouseEventArgs.viewportPosition Property

Parent Object: [MouseEventArgs](MouseEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MouseEventArgs.h>

## Description

Gets the coordinate of the mouse in viewport space, if the mouse is within a viewport. If the mouse is not over a viewport this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mouseEventArgs\_var" is a variable referencing a MouseEventArgs object. |

"mouseEventArgs\_var" is a variable referencing a MouseEventArgs object. ```` ``` #include <Core/UserInterface/MouseEventArgs.h>  // Get the value of the property. Ptr<Point2D> propertyValue = mouseEventArgs_var->viewportPosition(); ``` ```` |

## Property Value

This is a read only property whose value is a [Point2D](Point2D.htm).

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |