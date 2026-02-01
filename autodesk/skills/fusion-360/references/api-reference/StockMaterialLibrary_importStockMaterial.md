# StockMaterialLibrary.importStockMaterial Method![](../images/TestTubeLarge.png)

Parent Object: [StockMaterialLibrary](StockMaterialLibrary.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/StockMaterials/StockMaterialLibrary.h>

## Description

Import a given stockMaterial at a specific location. The stockMaterial will be stored in the library. Throws an error, if the given URL is read-only.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stockMaterialLibrary\_var" is a variable referencing a [StockMaterialLibrary](StockMaterialLibrary.htm) object.```` ``` returnValue = stockMaterialLibrary_var.importStockMaterial(stockMaterial, destinationUrl, stockMaterialName) ``` ```` |

"stockMaterialLibrary\_var" is a variable referencing a [StockMaterialLibrary](StockMaterialLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [URL](URL.htm) | Returns the URL of the newly imported stockMaterial, or null if the import failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stockMaterial | [StockMaterial](StockMaterial.htm) | The stockMaterial that should be imported. |
| destinationUrl | [URL](URL.htm) | The URL to the folder where to save the stockMaterial. |
| stockMaterialName | string | The name of the stockMaterial that should be created due to the import. The name can be extended if the asset already exists at given location to ensure a unique name. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |