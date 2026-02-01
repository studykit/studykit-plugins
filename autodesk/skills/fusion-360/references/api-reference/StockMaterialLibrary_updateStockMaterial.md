# StockMaterialLibrary.updateStockMaterial Method![](../images/TestTubeLarge.png)

Parent Object: [StockMaterialLibrary](StockMaterialLibrary.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/StockMaterials/StockMaterialLibrary.h>

## Description

Update a stockMaterial in the library. The library overrides the URL by given stockMaterial. Throws an error if the URL does not already point to an existing stockMaterial.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stockMaterialLibrary\_var" is a variable referencing a [StockMaterialLibrary](StockMaterialLibrary.htm) object.```` ``` returnValue = stockMaterialLibrary_var.updateStockMaterial(url, stockMaterial) ``` ```` |

"stockMaterialLibrary\_var" is a variable referencing a [StockMaterialLibrary](StockMaterialLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if asset was updated successfully, false otherwise. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| url | [URL](URL.htm) | The URL to the existing asset in the library that should be updated. |
| stockMaterial | [StockMaterial](StockMaterial.htm) | The stockMaterial that should be persisted. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |