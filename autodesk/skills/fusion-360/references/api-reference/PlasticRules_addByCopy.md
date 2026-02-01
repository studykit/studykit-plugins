# PlasticRules.addByCopy Method

Parent Object: [PlasticRules](PlasticRules.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/PlasticRules.h>

## Description

Creates a new plastic rule by copying an existing rule. The new rule can then be edited to define the rule characteristics you want.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plasticRules\_var" is a variable referencing a [PlasticRules](PlasticRules.htm) object.```` ``` returnValue = plasticRules_var.addByCopy(existingPlasticRule, name) ``` ```` |

"plasticRules\_var" is a variable referencing a [PlasticRules](PlasticRules.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PlasticRule](PlasticRule.htm) | Returns the new PlasticRule object or will assert in the case where it fails. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| existingPlasticRule | [PlasticRule](PlasticRule.htm) | The existing PlasticRule object you want to copy. This can be a rule from the library or the design. |
| name | string | The name to assign to the new plastic rule. This name must be unique with respect to other plastic rules in the design or library it's created in. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |