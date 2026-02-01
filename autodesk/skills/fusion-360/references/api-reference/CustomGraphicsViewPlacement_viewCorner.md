# CustomGraphicsViewPlacement.viewCorner Property

Parent Object: [CustomGraphicsViewPlacement](CustomGraphicsViewPlacement.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsViewPlacement.h>

## Description

Gets and sets which corner the graphics are positioned relative to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsViewPlacement\_var" is a variable referencing a CustomGraphicsViewPlacement object. |

"customGraphicsViewPlacement\_var" is a variable referencing a CustomGraphicsViewPlacement object. ```` ``` #include <Fusion/Graphics/CustomGraphicsViewPlacement.h>  // Get the value of the property. ViewCorners propertyValue = customGraphicsViewPlacement_var->viewCorner();  // Set the value of the property, where value_var is a ViewCorners. bool returnValue = customGraphicsViewPlacement_var->viewCorner(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ViewCorners](ViewCorners.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |