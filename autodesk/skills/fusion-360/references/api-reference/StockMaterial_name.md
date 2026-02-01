# StockMaterial.name Property![](../images/TestTubeLarge.png)

Parent Object: [StockMaterial](StockMaterial.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/StockMaterials/StockMaterial.h>

## Description

Gets and sets the name of the stock material.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stockMaterial\_var" is a variable referencing a StockMaterial object. |

"stockMaterial\_var" is a variable referencing a StockMaterial object. ```` ``` #include <Cam/StockMaterials/StockMaterial.h>  // Get the value of the property. string propertyValue = stockMaterial_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = stockMaterial_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |