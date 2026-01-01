# PlasticRules.item Method

Parent Object: [PlasticRules](PlasticRules.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/PlasticRules.h>

## Description

Function that returns the specified plastic rule using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plasticRules\_var" is a variable referencing a [PlasticRules](PlasticRules.htm) object.```` ``` returnValue = plasticRules_var.item(index) ``` ```` |

"plasticRules\_var" is a variable referencing a [PlasticRules](PlasticRules.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PlasticRule](PlasticRule.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |