# ZebraAnalyses.item Method

Parent Object: [ZebraAnalyses](ZebraAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ZebraAnalyses.h>

## Description

A method that returns the specified ZebraAnalysis object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"zebraAnalyses\_var" is a variable referencing a [ZebraAnalyses](ZebraAnalyses.htm) object.```` ``` returnValue = zebraAnalyses_var.item(index) ``` ```` |

"zebraAnalyses\_var" is a variable referencing a [ZebraAnalyses](ZebraAnalyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ZebraAnalysis](ZebraAnalysis.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |