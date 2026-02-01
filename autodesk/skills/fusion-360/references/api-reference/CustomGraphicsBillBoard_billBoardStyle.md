# CustomGraphicsBillBoard.billBoardStyle Property

Parent Object: [CustomGraphicsBillBoard](CustomGraphicsBillBoard.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsBillBoard.h>

## Description

Specifies the type of billboarding to use. When a new CustomGraphicsBillBoard object is created this defaults to ScreenBillBoardStyle so the graphics will all be facing the view plane. It can also be set to an arbitrary plane by setting this to AxialBillBoardStyle and can be defined so that it never appear backwards by setting it to RightReadingBillBoardStyle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsBillBoard\_var" is a variable referencing a CustomGraphicsBillBoard object. |

"customGraphicsBillBoard\_var" is a variable referencing a CustomGraphicsBillBoard object. ```` ``` #include <Fusion/Graphics/CustomGraphicsBillBoard.h>  // Get the value of the property. CustomGraphicsBillBoardStyles propertyValue = customGraphicsBillBoard_var->billBoardStyle();  // Set the value of the property, where value_var is a CustomGraphicsBillBoardStyles. bool returnValue = customGraphicsBillBoard_var->billBoardStyle(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [CustomGraphicsBillBoardStyles](CustomGraphicsBillBoardStyles.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |