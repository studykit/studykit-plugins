# CustomGraphicsCurve.parent Property

Parent Object: [CustomGraphicsCurve](CustomGraphicsCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsCurve.h>

## Description

Returns the parent Component for a top-level group or the CustomGraphicsGroup object for graphics entities and child groups.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsCurve\_var" is a variable referencing a CustomGraphicsCurve object. |

"customGraphicsCurve\_var" is a variable referencing a CustomGraphicsCurve object. ```` ``` #include <Fusion/Graphics/CustomGraphicsCurve.h>  // Get the value of the property. Ptr<Base> propertyValue = customGraphicsCurve_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |