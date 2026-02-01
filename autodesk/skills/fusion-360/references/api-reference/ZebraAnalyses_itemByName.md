# ZebraAnalyses.itemByName Method

Parent Object: [ZebraAnalyses](ZebraAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ZebraAnalyses.h>

## Description

A method that returns the specified ZebraAnalysis object using the name of the analysis as it is displayed in the browser.

## Syntax

* [Python](#Python)
* [C++](#C++)

"zebraAnalyses\_var" is a variable referencing a [ZebraAnalyses](ZebraAnalyses.htm) object.```` ``` returnValue = zebraAnalyses_var.itemByName(name) ``` ```` |

"zebraAnalyses\_var" is a variable referencing a [ZebraAnalyses](ZebraAnalyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ZebraAnalysis](ZebraAnalysis.htm) | Returns the specified item or null if an invalid name was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the ZebraAnalysis object as it is displayed in the browser. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |