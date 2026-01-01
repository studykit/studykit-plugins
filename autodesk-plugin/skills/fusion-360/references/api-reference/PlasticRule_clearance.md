# PlasticRule.clearance Property

Parent Object: [PlasticRule](PlasticRule.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/PlasticRule.h>

## Description

The clearance used for plastic features. When using a float to set the value, it is defined in centimeters. When using a string to set the expression, the units can be defined as part of the expression or it defaults to the units associated with the rule if no units are specified.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plasticRule\_var" is a variable referencing a PlasticRule object. |

"plasticRule\_var" is a variable referencing a PlasticRule object. ```` ``` #include <Fusion/Plastic/PlasticRule.h>  // Get the value of the property. Ptr<PlasticRuleValue> propertyValue = plasticRule_var->clearance(); ``` ```` |

## Property Value

This is a read only property whose value is a [PlasticRuleValue](PlasticRuleValue.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |