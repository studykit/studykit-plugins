# AccessibilityAnalyses.item Method

Parent Object: [AccessibilityAnalyses](AccessibilityAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/AccessibilityAnalyses.h>

## Description

A method that returns the specified AccessibilityAnalysis object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"accessibilityAnalyses\_var" is a variable referencing an [AccessibilityAnalyses](AccessibilityAnalyses.htm) object.```` ``` returnValue = accessibilityAnalyses_var.item(index) ``` ```` |

"accessibilityAnalyses\_var" is a variable referencing an [AccessibilityAnalyses](AccessibilityAnalyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [AccessibilityAnalysis](AccessibilityAnalysis.htm) | Returns the specified item or null if an invalid index was specified. |

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