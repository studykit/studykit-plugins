# ArrangeResultEnvelopes.item Method

Parent Object: [ArrangeResultEnvelopes](ArrangeResultEnvelopes.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeResultEnvelopes.h>

## Description

Returns the specified Arrange envelope result using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeResultEnvelopes\_var" is a variable referencing an [ArrangeResultEnvelopes](ArrangeResultEnvelopes.htm) object.```` ``` returnValue = arrangeResultEnvelopes_var.item(index) ``` ```` |

"arrangeResultEnvelopes\_var" is a variable referencing an [ArrangeResultEnvelopes](ArrangeResultEnvelopes.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ArrangeResultEnvelope](ArrangeResultEnvelope.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |