# CustomGraphicsBillBoard.axis Property

Parent Object: [CustomGraphicsBillBoard](CustomGraphicsBillBoard.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsBillBoard.h>

## Description

When the billBoardStyle property is set to AxialBillBoardStyle, this is used to control the direction of the graphics. Otherwise it uses the x axis of the view.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsBillBoard\_var" is a variable referencing a CustomGraphicsBillBoard object. |

"customGraphicsBillBoard\_var" is a variable referencing a CustomGraphicsBillBoard object. ```` ``` #include <Fusion/Graphics/CustomGraphicsBillBoard.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = customGraphicsBillBoard_var->axis();  // Set the value of the property, where value_var is a Vector3D. bool returnValue = customGraphicsBillBoard_var->axis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |