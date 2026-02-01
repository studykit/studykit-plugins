# Analyses.item Method

Parent Object: [Analyses](Analyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Analyses.h>

## Description

A method that returns the specified Analysis using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"analyses\_var" is a variable referencing an [Analyses](Analyses.htm) object.```` ``` returnValue = analyses_var.item(index) ``` ```` |

"analyses\_var" is a variable referencing an [Analyses](Analyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Analysis](Analysis.htm) | Returns the specified item or null if an invalid index was specified. |

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