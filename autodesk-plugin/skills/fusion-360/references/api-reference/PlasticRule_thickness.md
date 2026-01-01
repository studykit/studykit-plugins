# PlasticRule.thickness Property

Parent Object: [PlasticRule](PlasticRule.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/PlasticRule.h>

## Description

The thickness used for plastic features. This value must be within the range specified by the minimumThickness and maximumThickness properties. This is used by the plastic commands when a wall thickness is needed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plasticRule\_var" is a variable referencing a PlasticRule object.  ```` ``` # Get the value of the property. propertyValue = plasticRule_var.thickness ``` ```` |

"plasticRule\_var" is a variable referencing a PlasticRule object. ```` ``` #include <Fusion/Plastic/PlasticRule.h>  // Get the value of the property. Ptr<PlasticRuleValue> propertyValue = plasticRule_var->thickness(); ``` ```` |

## Property Value

This is a read only property whose value is a [PlasticRuleValue](PlasticRuleValue.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |