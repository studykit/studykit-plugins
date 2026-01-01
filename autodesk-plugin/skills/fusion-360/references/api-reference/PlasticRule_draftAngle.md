# PlasticRule.draftAngle Property

Parent Object: [PlasticRule](PlasticRule.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/PlasticRule.h>

## Description

The draft angle used for plastic features. When using a float to set the value, it is defined in radians. When using a string to set the expression it uses degrees.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plasticRule\_var" is a variable referencing a PlasticRule object. |

"plasticRule\_var" is a variable referencing a PlasticRule object. ```` ``` #include <Fusion/Plastic/PlasticRule.h>  // Get the value of the property. Ptr<PlasticRuleValue> propertyValue = plasticRule_var->draftAngle(); ``` ```` |

## Property Value

This is a read only property whose value is a [PlasticRuleValue](PlasticRuleValue.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |