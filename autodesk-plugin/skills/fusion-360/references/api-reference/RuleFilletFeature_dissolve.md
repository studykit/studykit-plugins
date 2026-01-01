# RuleFilletFeature.dissolve Method

Parent Object: [RuleFilletFeature](RuleFilletFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuleFilletFeature.h>

## Description

Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruleFilletFeature\_var" is a variable referencing a [RuleFilletFeature](RuleFilletFeature.htm) object.```` ``` returnValue = ruleFilletFeature_var.dissolve() ``` ```` |

"ruleFilletFeature\_var" is a variable referencing a [RuleFilletFeature](RuleFilletFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns a bool indicating if the dissolve was successful or not. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |