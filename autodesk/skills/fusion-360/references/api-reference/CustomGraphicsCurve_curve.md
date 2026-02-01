# CustomGraphicsCurve.curve Property

Parent Object: [CustomGraphicsCurve](CustomGraphicsCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsCurve.h>

## Description

Gets and sets the curve associated with this graphics entity. Any of the curve types derived from Curve3D is valid except for InfiniteLine3D.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsCurve\_var" is a variable referencing a CustomGraphicsCurve object. |

"customGraphicsCurve\_var" is a variable referencing a CustomGraphicsCurve object. ```` ``` #include <Fusion/Graphics/CustomGraphicsCurve.h>  // Get the value of the property. Ptr<Curve3D> propertyValue = customGraphicsCurve_var->curve();  // Set the value of the property, where value_var is a Curve3D. bool returnValue = customGraphicsCurve_var->curve(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Curve3D](Curve3D.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |