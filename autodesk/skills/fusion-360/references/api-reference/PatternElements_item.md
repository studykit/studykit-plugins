# PatternElements.item Method

Parent Object: [PatternElements](PatternElements.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatternElements.h>

## Description

Function that returns the specified pattern element using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patternElements\_var" is a variable referencing a [PatternElements](PatternElements.htm) object.```` ``` returnValue = patternElements_var.item(index) ``` ```` |

"patternElements\_var" is a variable referencing a [PatternElements](PatternElements.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PatternElement](PatternElement.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |