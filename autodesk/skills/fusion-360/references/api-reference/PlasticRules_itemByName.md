# PlasticRules.itemByName Method

Parent Object: [PlasticRules](PlasticRules.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/PlasticRules.h>

## Description

Function that returns the specified plastic rule using the name of the rule.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plasticRules\_var" is a variable referencing a [PlasticRules](PlasticRules.htm) object.```` ``` returnValue = plasticRules_var.itemByName(name) ``` ```` |

"plasticRules\_var" is a variable referencing a [PlasticRules](PlasticRules.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PlasticRule](PlasticRule.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the rule within the collection to return. This is the name seen in the Plastic Rules dialog. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |