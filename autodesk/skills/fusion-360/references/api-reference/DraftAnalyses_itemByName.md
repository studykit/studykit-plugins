# DraftAnalyses.itemByName Method

Parent Object: [DraftAnalyses](DraftAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/DraftAnalyses.h>

## Description

A method that returns the specified DraftAnalysis object using the name of the analysis as displayed in the browser.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftAnalyses\_var" is a variable referencing a [DraftAnalyses](DraftAnalyses.htm) object.```` ``` returnValue = draftAnalyses_var.itemByName(name) ``` ```` |

"draftAnalyses\_var" is a variable referencing a [DraftAnalyses](DraftAnalyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DraftAnalysis](DraftAnalysis.htm) | Returns the specified item or null if an invalid name was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the DraftAnalysis object as displayed in the browser. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |