# RuleFilletFeature.linkedFeatures Property

Parent Object: [RuleFilletFeature](RuleFilletFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuleFilletFeature.h>

## Description

Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruleFilletFeature\_var" is a variable referencing a RuleFilletFeature object. |

"ruleFilletFeature\_var" is a variable referencing a RuleFilletFeature object. ```` ``` #include <Fusion/Features/RuleFilletFeature.h>  // Get the value of the property. Ptr<FeatureList> propertyValue = ruleFilletFeature_var->linkedFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [FeatureList](FeatureList.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |