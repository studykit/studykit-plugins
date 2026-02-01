# Canvas.isLightBulbOn Property

Parent Object: [Canvas](Canvas.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Canvas.h>

## Description

Gets and sets if the light bulb of this canvas as displayed in the browser is on or off.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvas\_var" is a variable referencing a Canvas object.  ```` ``` # Get the value of the property. propertyValue = canvas_var.isLightBulbOn  # Set the value of the property. canvas_var.isLightBulbOn = propertyValue ``` ```` |

"canvas\_var" is a variable referencing a Canvas object. ```` ``` #include <Fusion/Image/Canvas.h>  // Get the value of the property. boolean propertyValue = canvas_var->isLightBulbOn();  // Set the value of the property, where value_var is a boolean. bool returnValue = canvas_var->isLightBulbOn(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |