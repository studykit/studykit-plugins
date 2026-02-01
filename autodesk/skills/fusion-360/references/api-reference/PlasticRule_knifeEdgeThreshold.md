# PlasticRule.knifeEdgeThreshold Property

Parent Object: [PlasticRule](PlasticRule.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/PlasticRule.h>

## Description

The minimal thickness where an edge is considered a knife edge. This is used by the Design Advice command when analyzing the part for manufacturability.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plasticRule\_var" is a variable referencing a PlasticRule object.  ```` ``` # Get the value of the property. propertyValue = plasticRule_var.knifeEdgeThreshold ``` ```` |

"plasticRule\_var" is a variable referencing a PlasticRule object. ```` ``` #include <Fusion/Plastic/PlasticRule.h>  // Get the value of the property. Ptr<PlasticRuleValue> propertyValue = plasticRule_var->knifeEdgeThreshold(); ``` ```` |

## Property Value

This is a read only property whose value is a [PlasticRuleValue](PlasticRuleValue.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |