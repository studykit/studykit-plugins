# CanvasInput.plane Property

Parent Object: [CanvasInput](CanvasInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/CanvasInput.h>

## Description

Returns a Plane object that is obtained from the planar face or construction plane and defines the parameter space the canvas is positioned relative to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvasInput\_var" is a variable referencing a CanvasInput object. |

"canvasInput\_var" is a variable referencing a CanvasInput object. ```` ``` #include <Fusion/Image/CanvasInput.h>  // Get the value of the property. Ptr<Plane> propertyValue = canvasInput_var->plane(); ``` ```` |

## Property Value

This is a read only property whose value is a [Plane](Plane.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |