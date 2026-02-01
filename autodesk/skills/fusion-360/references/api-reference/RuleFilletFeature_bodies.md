# RuleFilletFeature.bodies Property

Parent Object: [RuleFilletFeature](RuleFilletFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuleFilletFeature.h>

## Description

Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruleFilletFeature\_var" is a variable referencing a RuleFilletFeature object.  ```` ``` # Get the value of the property. propertyValue = ruleFilletFeature_var.bodies ``` ```` |

"ruleFilletFeature\_var" is a variable referencing a RuleFilletFeature object. ```` ``` #include <Fusion/Features/RuleFilletFeature.h>  // Get the value of the property. Ptr<BRepBodies> propertyValue = ruleFilletFeature_var->bodies(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBodies](BRepBodies.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |