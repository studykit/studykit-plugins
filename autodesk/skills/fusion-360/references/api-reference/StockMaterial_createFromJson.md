# StockMaterial.createFromJson Method![](../images/TestTubeLarge.png)

Parent Object: [StockMaterial](StockMaterial.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/StockMaterials/StockMaterial.h>

## Description

Creates a StockMaterial object from given JSON string.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [StockMaterial](StockMaterial.htm) | Returns the newly created StockMaterial. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| json | string | The JSON should fully define the StockMaterial and contain all StockMaterial parameters. If the JSON contains more than one StockMaterial, only the first StockMaterial is loaded. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |