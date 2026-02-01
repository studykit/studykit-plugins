# RuleFilletFeature.isSuppressed Property

Parent Object: [RuleFilletFeature](RuleFilletFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuleFilletFeature.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruleFilletFeature\_var" is a variable referencing a RuleFilletFeature object. |

"ruleFilletFeature\_var" is a variable referencing a RuleFilletFeature object. ```` ``` #include <Fusion/Features/RuleFilletFeature.h>  // Get the value of the property. boolean propertyValue = ruleFilletFeature_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = ruleFilletFeature_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |