# PlasticRuleValue.value Property

Parent Object: [PlasticRuleValue](PlasticRuleValue.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/PlasticRuleValue.h>

## Description

Gets and sets the value of the plastic rule value in centimeters. Setting this value will create a new expression that is equivalent to the new value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plasticRuleValue\_var" is a variable referencing a PlasticRuleValue object. |

"plasticRuleValue\_var" is a variable referencing a PlasticRuleValue object. ```` ``` #include <Fusion/Plastic/PlasticRuleValue.h>  // Get the value of the property. double propertyValue = plasticRuleValue_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = plasticRuleValue_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |