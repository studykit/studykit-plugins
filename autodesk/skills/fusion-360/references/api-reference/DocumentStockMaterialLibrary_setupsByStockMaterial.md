# DocumentStockMaterialLibrary.setupsByStockMaterial Method![](../images/TestTubeLarge.png)

Parent Object: [DocumentStockMaterialLibrary](DocumentStockMaterialLibrary.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/StockMaterials/DocumentStockMaterialLibrary.h>

## Description

Returns all setups that use the given StockMaterial. The StockMaterial must exist in the document StockMaterial library. Raises an error if the StockMaterial is not in the document.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentStockMaterialLibrary\_var" is a variable referencing a [DocumentStockMaterialLibrary](DocumentStockMaterialLibrary.htm) object.```` ``` returnValue = documentStockMaterialLibrary_var.setupsByStockMaterial(stockMaterial) ``` ```` |

"documentStockMaterialLibrary\_var" is a variable referencing a [DocumentStockMaterialLibrary](DocumentStockMaterialLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Setup](Setup.htm)[] | Returns setups using a specific StockMaterial. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stockMaterial | [StockMaterial](StockMaterial.htm) | The StockMaterial to search for setups. The StockMaterial must exist in the document. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |