# CustomGraphicsCurve.isVisible Property

Parent Object: [CustomGraphicsCurve](CustomGraphicsCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsCurve.h>

## Description

Gets and sets if the graphics entity is visible in the graphics window. By default, when a new entity is created it is visible.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsCurve\_var" is a variable referencing a CustomGraphicsCurve object. |

"customGraphicsCurve\_var" is a variable referencing a CustomGraphicsCurve object. ```` ``` #include <Fusion/Graphics/CustomGraphicsCurve.h>  // Get the value of the property. boolean propertyValue = customGraphicsCurve_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = customGraphicsCurve_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |