# Occurrences.item Method

Parent Object: [Occurrences](Occurrences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrences.h>

## Description

Function that returns the specified occurrence using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrences\_var" is a variable referencing an [Occurrences](Occurrences.htm) object.```` ``` returnValue = occurrences_var.item(index) ``` ```` |

"occurrences\_var" is a variable referencing an [Occurrences](Occurrences.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Occurrence](Occurrence.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |