# StockMaterialLibrary.stockMaterialAtURL Method![](../images/TestTubeLarge.png)

Parent Object: [StockMaterialLibrary](StockMaterialLibrary.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/StockMaterials/StockMaterialLibrary.h>

## Description

Get a specific stockMaterial by the given URL. Returns null, if the URL does not exist.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stockMaterialLibrary\_var" is a variable referencing a [StockMaterialLibrary](StockMaterialLibrary.htm) object.```` ``` returnValue = stockMaterialLibrary_var.stockMaterialAtURL(url) ``` ```` |

"stockMaterialLibrary\_var" is a variable referencing a [StockMaterialLibrary](StockMaterialLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [StockMaterial](StockMaterial.htm) | Returns the stockMaterial for a valid URL, returns null otherwise. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| url | [URL](URL.htm) | The URL to the stockMaterial to be loaded. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |