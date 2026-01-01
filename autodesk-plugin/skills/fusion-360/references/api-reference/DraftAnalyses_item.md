# DraftAnalyses.item Method

Parent Object: [DraftAnalyses](DraftAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/DraftAnalyses.h>

## Description

A method that returns the specified DraftAnalysis object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftAnalyses\_var" is a variable referencing a [DraftAnalyses](DraftAnalyses.htm) object.```` ``` returnValue = draftAnalyses_var.item(index) ``` ```` |

"draftAnalyses\_var" is a variable referencing a [DraftAnalyses](DraftAnalyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DraftAnalysis](DraftAnalysis.htm) | Returns the specified item or null if an invalid index was specified. |

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