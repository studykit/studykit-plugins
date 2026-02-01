# CustomGraphicsLines.lineStyleScale Property

Parent Object: [CustomGraphicsLines](CustomGraphicsLines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsLines.h>

## Description

Defines the scale as it relates to how the line style is applied. The effect is to shrink or expand the line style as it is applied to the line. This does not affect the line width.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsLines\_var" is a variable referencing a CustomGraphicsLines object. |

"customGraphicsLines\_var" is a variable referencing a CustomGraphicsLines object. ```` ``` #include <Fusion/Graphics/CustomGraphicsLines.h>  // Get the value of the property. double propertyValue = customGraphicsLines_var->lineStyleScale();  // Set the value of the property, where value_var is a double. bool returnValue = customGraphicsLines_var->lineStyleScale(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |