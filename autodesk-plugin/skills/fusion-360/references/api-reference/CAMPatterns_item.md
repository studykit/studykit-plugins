# CAMPatterns.item Method

Parent Object: [CAMPatterns](CAMPatterns.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMPatterns.h>

## Description

Function that returns the specified pattern using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMPatterns\_var" is a variable referencing a [CAMPatterns](CAMPatterns.htm) object.```` ``` returnValue = cAMPatterns_var.item(index) ``` ```` |

"cAMPatterns\_var" is a variable referencing a [CAMPatterns](CAMPatterns.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CAMPattern](CAMPattern.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |