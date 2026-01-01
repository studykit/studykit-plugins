# CustomGraphicsCurve.weight Property

Parent Object: [CustomGraphicsCurve](CustomGraphicsCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsCurve.h>

## Description

Defines the thickness of the curve in pixels.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsCurve\_var" is a variable referencing a CustomGraphicsCurve object. |

"customGraphicsCurve\_var" is a variable referencing a CustomGraphicsCurve object. ```` ``` #include <Fusion/Graphics/CustomGraphicsCurve.h>  // Get the value of the property. double propertyValue = customGraphicsCurve_var->weight();  // Set the value of the property, where value_var is a double. bool returnValue = customGraphicsCurve_var->weight(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |