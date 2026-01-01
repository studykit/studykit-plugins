# CanvasInput.planarEntity Property

Parent Object: [CanvasInput](CanvasInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/CanvasInput.h>

## Description

Gets and sets the plane the canvas is associated with. This can be either a planar Face or a construction plane. In a direct modeling design or the canvas is being created in a base feature, this can be a Plane object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvasInput\_var" is a variable referencing a CanvasInput object. |

"canvasInput\_var" is a variable referencing a CanvasInput object. ```` ``` #include <Fusion/Image/CanvasInput.h>  // Get the value of the property. Ptr<Base> propertyValue = canvasInput_var->planarEntity();  // Set the value of the property, where value_var is a Base. bool returnValue = canvasInput_var->planarEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |