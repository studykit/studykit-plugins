# PlasticRuleValue.objectType Property

Parent Object: [PlasticRuleValue](PlasticRuleValue.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/PlasticRuleValue.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plasticRuleValue\_var" is a variable referencing a PlasticRuleValue object.  ```` ``` # Get the value of the property. propertyValue = plasticRuleValue_var.objectType ``` ```` |

"plasticRuleValue\_var" is a variable referencing a PlasticRuleValue object. ```` ``` #include <Fusion/Plastic/PlasticRuleValue.h>  // Get the value of the property. string propertyValue = plasticRuleValue_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |