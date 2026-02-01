# CustomGraphicsCurve.lineStylePattern Property

Parent Object: [CustomGraphicsCurve](CustomGraphicsCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsCurve.h>

## Description

The line style to apply to the curve. The default is to draw the curve using continuous line style.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsCurve\_var" is a variable referencing a CustomGraphicsCurve object. |

"customGraphicsCurve\_var" is a variable referencing a CustomGraphicsCurve object. ```` ``` #include <Fusion/Graphics/CustomGraphicsCurve.h>  // Get the value of the property. LineStylePatterns propertyValue = customGraphicsCurve_var->lineStylePattern();  // Set the value of the property, where value_var is a LineStylePatterns. bool returnValue = customGraphicsCurve_var->lineStylePattern(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [LineStylePatterns](LineStylePatterns.htm).

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |