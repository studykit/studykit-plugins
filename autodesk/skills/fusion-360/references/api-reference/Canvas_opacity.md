# Canvas.opacity Property

Parent Object: [Canvas](Canvas.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Canvas.h>

## Description

Gets and sets the opacity of the canvas where 0 is completely transparent and 100 is completely opaque. Setting this property to a value outside the range of 0-100 will result in the value being set to the closest valid value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvas\_var" is a variable referencing a Canvas object. |

"canvas\_var" is a variable referencing a Canvas object. ```` ``` #include <Fusion/Image/Canvas.h>  // Get the value of the property. integer propertyValue = canvas_var->opacity();  // Set the value of the property, where value_var is an integer. bool returnValue = canvas_var->opacity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |