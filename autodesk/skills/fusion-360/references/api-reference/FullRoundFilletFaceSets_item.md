# FullRoundFilletFaceSets.item Method

Parent Object: [FullRoundFilletFaceSets](FullRoundFilletFaceSets.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FullRoundFilletFaceSets.h>

## Description

Function that returns the specified full round fillet face set using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fullRoundFilletFaceSets\_var" is a variable referencing a [FullRoundFilletFaceSets](FullRoundFilletFaceSets.htm) object.```` ``` returnValue = fullRoundFilletFaceSets_var.item(index) ``` ```` |

"fullRoundFilletFaceSets\_var" is a variable referencing a [FullRoundFilletFaceSets](FullRoundFilletFaceSets.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [FullRoundFilletFaceSet](FullRoundFilletFaceSet.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |