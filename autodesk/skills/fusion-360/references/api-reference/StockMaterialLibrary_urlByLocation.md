# StockMaterialLibrary.urlByLocation Method![](../images/TestTubeLarge.png)

Parent Object: [StockMaterialLibrary](StockMaterialLibrary.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/StockMaterials/StockMaterialLibrary.h>

## Description

Get the URL for a given LibraryLocations.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stockMaterialLibrary\_var" is a variable referencing a [StockMaterialLibrary](StockMaterialLibrary.htm) object.```` ``` returnValue = stockMaterialLibrary_var.urlByLocation(location) ``` ```` |

"stockMaterialLibrary\_var" is a variable referencing a [StockMaterialLibrary](StockMaterialLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [URL](URL.htm) | Returns the URL for given location. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| location | [LibraryLocations](LibraryLocations.htm) | The LibraryLocations to be converted into an URL. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |