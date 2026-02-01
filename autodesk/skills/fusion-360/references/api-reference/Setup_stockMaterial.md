# Setup.stockMaterial Property![](../images/TestTubeLarge.png)

Parent Object: [Setup](Setup.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/CAM/Setup.h>

## Description

Gets/ and sets the Stock material associated with the setup.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setup\_var" is a variable referencing a Setup object. |

"setup\_var" is a variable referencing a Setup object. ```` ``` #include <Cam/CAM/Setup.h>  // Get the value of the property. Ptr<StockMaterial> propertyValue = setup_var->stockMaterial();  // Set the value of the property, where value_var is a StockMaterial. bool returnValue = setup_var->stockMaterial(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [StockMaterial](StockMaterial.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |