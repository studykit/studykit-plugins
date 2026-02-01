# SectionAnalyses.item Method

Parent Object: [SectionAnalyses](SectionAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SectionAnalyses.h>

## Description

A method that returns the specified SectionAnalysis object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sectionAnalyses\_var" is a variable referencing a [SectionAnalyses](SectionAnalyses.htm) object.```` ``` returnValue = sectionAnalyses_var.item(index) ``` ```` |

"sectionAnalyses\_var" is a variable referencing a [SectionAnalyses](SectionAnalyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SectionAnalysis](SectionAnalysis.htm) | Returns the specified item or null if an invalid index was specified. |

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