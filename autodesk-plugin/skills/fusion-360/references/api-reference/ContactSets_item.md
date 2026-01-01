# ContactSets.item Method

Parent Object: [ContactSets](ContactSets.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/ContactSets.h>

## Description

Returns the specified contact set using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"contactSets\_var" is a variable referencing a [ContactSets](ContactSets.htm) object.```` ``` returnValue = contactSets_var.item(index) ``` ```` |

"contactSets\_var" is a variable referencing a [ContactSets](ContactSets.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ContactSet](ContactSet.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |