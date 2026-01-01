# CustomGraphicsCurve.lineStyleScale Property

Parent Object: [CustomGraphicsCurve](CustomGraphicsCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsCurve.h>

## Description

Defines the scale as it relates to how the line style is applied. The effect is to shrink or expand the line style as it is applied to the line. This does not affect the line width.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsCurve\_var" is a variable referencing a CustomGraphicsCurve object. |

"customGraphicsCurve\_var" is a variable referencing a CustomGraphicsCurve object. ```` ``` #include <Fusion/Graphics/CustomGraphicsCurve.h>  // Get the value of the property. double propertyValue = customGraphicsCurve_var->lineStyleScale();  // Set the value of the property, where value_var is a double. bool returnValue = customGraphicsCurve_var->lineStyleScale(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |