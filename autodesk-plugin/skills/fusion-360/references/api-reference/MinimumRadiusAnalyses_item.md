# MinimumRadiusAnalyses.item Method

Parent Object: [MinimumRadiusAnalyses](MinimumRadiusAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/MinimumRadiusAnalyses.h>

## Description

A method that returns the specified MinimumRadiusAnalysis object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"minimumRadiusAnalyses\_var" is a variable referencing a [MinimumRadiusAnalyses](MinimumRadiusAnalyses.htm) object.```` ``` returnValue = minimumRadiusAnalyses_var.item(index) ``` ```` |

"minimumRadiusAnalyses\_var" is a variable referencing a [MinimumRadiusAnalyses](MinimumRadiusAnalyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MinimumRadiusAnalysis](MinimumRadiusAnalysis.htm) | Returns the specified item or null if an invalid index was specified. |

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