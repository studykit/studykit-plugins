# RuleFilletFeatures.item Method

Parent Object: [RuleFilletFeatures](RuleFilletFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuleFilletFeatures.h>

## Description

Function that returns the specified rule fillet feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruleFilletFeatures\_var" is a variable referencing a [RuleFilletFeatures](RuleFilletFeatures.htm) object.```` ``` returnValue = ruleFilletFeatures_var.item(index) ``` ```` |

"ruleFilletFeatures\_var" is a variable referencing a [RuleFilletFeatures](RuleFilletFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RuleFilletFeature](RuleFilletFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |