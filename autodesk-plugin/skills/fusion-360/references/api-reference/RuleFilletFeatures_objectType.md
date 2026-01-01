# RuleFilletFeatures.objectType Property

Parent Object: [RuleFilletFeatures](RuleFilletFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuleFilletFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruleFilletFeatures\_var" is a variable referencing a RuleFilletFeatures object.  ```` ``` # Get the value of the property. propertyValue = ruleFilletFeatures_var.objectType ``` ```` |

"ruleFilletFeatures\_var" is a variable referencing a RuleFilletFeatures object. ```` ``` #include <Fusion/Features/RuleFilletFeatures.h>  // Get the value of the property. string propertyValue = ruleFilletFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |