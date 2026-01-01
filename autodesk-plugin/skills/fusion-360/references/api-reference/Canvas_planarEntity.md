# Canvas.planarEntity Property

Parent Object: [Canvas](Canvas.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Canvas.h>

## Description

Gets and sets the plane the canvas is associated with. This can be either a planar Face or a construction plane. In a direct modeling design or the canvas is being created in a base feature, this can be a Plane object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvas\_var" is a variable referencing a Canvas object. |

"canvas\_var" is a variable referencing a Canvas object. ```` ``` #include <Fusion/Image/Canvas.h>  // Get the value of the property. Ptr<Base> propertyValue = canvas_var->planarEntity();  // Set the value of the property, where value_var is a Base. bool returnValue = canvas_var->planarEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |