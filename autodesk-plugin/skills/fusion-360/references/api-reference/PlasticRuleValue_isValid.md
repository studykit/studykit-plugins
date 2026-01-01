# PlasticRuleValue.isValid Property

Parent Object: [PlasticRuleValue](PlasticRuleValue.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/PlasticRuleValue.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plasticRuleValue\_var" is a variable referencing a PlasticRuleValue object. |

"plasticRuleValue\_var" is a variable referencing a PlasticRuleValue object. ```` ``` #include <Fusion/Plastic/PlasticRuleValue.h>  // Get the value of the property. boolean propertyValue = plasticRuleValue_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |