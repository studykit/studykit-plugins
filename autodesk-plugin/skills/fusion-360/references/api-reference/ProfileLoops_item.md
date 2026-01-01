# ProfileLoops.item Method

Parent Object: [ProfileLoops](ProfileLoops.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ProfileLoops.h>

## Description

Function that returns the specified profile loop using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profileLoops\_var" is a variable referencing a [ProfileLoops](ProfileLoops.htm) object.```` ``` returnValue = profileLoops_var.item(index) ``` ```` |

"profileLoops\_var" is a variable referencing a [ProfileLoops](ProfileLoops.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ProfileLoop](ProfileLoop.htm) | Returns the specified item or null if an invalid index was specified. |

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