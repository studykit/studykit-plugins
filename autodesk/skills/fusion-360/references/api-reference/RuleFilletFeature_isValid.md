# RuleFilletFeature.isValid Property

Parent Object: [RuleFilletFeature](RuleFilletFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuleFilletFeature.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruleFilletFeature\_var" is a variable referencing a RuleFilletFeature object. |

"ruleFilletFeature\_var" is a variable referencing a RuleFilletFeature object. ```` ``` #include <Fusion/Features/RuleFilletFeature.h>  // Get the value of the property. boolean propertyValue = ruleFilletFeature_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |