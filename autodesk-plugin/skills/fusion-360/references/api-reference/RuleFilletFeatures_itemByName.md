# RuleFilletFeatures.itemByName Method

Parent Object: [RuleFilletFeatures](RuleFilletFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuleFilletFeatures.h>

## Description

Function that returns the specified rule fillet feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruleFilletFeatures\_var" is a variable referencing a [RuleFilletFeatures](RuleFilletFeatures.htm) object.```` ``` returnValue = ruleFilletFeatures_var.itemByName(name) ``` ```` |

"ruleFilletFeatures\_var" is a variable referencing a [RuleFilletFeatures](RuleFilletFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RuleFilletFeature](RuleFilletFeature.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the feature within the collection to return. This is the name seen in the timeline. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |