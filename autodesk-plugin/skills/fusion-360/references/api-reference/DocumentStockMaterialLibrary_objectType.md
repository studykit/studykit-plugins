# DocumentStockMaterialLibrary.objectType Property![](../images/TestTubeLarge.png)

Parent Object: [DocumentStockMaterialLibrary](DocumentStockMaterialLibrary.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/StockMaterials/DocumentStockMaterialLibrary.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentStockMaterialLibrary\_var" is a variable referencing a DocumentStockMaterialLibrary object. |

"documentStockMaterialLibrary\_var" is a variable referencing a DocumentStockMaterialLibrary object. ```` ``` #include <Cam/StockMaterials/DocumentStockMaterialLibrary.h>  // Get the value of the property. string propertyValue = documentStockMaterialLibrary_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |