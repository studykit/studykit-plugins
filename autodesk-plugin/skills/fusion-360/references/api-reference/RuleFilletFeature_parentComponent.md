# RuleFilletFeature.parentComponent Property

Parent Object: [RuleFilletFeature](RuleFilletFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuleFilletFeature.h>

## Description

Returns the parent component that owns this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruleFilletFeature\_var" is a variable referencing a RuleFilletFeature object. |

"ruleFilletFeature\_var" is a variable referencing a RuleFilletFeature object. ```` ``` #include <Fusion/Features/RuleFilletFeature.h>  // Get the value of the property. Ptr<Component> propertyValue = ruleFilletFeature_var->parentComponent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |