# Canvas.isDisplayedThrough Property

Parent Object: [Canvas](Canvas.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Canvas.h>

## Description

Controls if the image is visible through the model or not.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvas\_var" is a variable referencing a Canvas object. |

"canvas\_var" is a variable referencing a Canvas object. ```` ``` #include <Fusion/Image/Canvas.h>  // Get the value of the property. boolean propertyValue = canvas_var->isDisplayedThrough();  // Set the value of the property, where value_var is a boolean. bool returnValue = canvas_var->isDisplayedThrough(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |