# PlasticRules.isValid Property

Parent Object: [PlasticRules](PlasticRules.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/PlasticRules.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plasticRules\_var" is a variable referencing a PlasticRules object. |

"plasticRules\_var" is a variable referencing a PlasticRules object. ```` ``` #include <Fusion/Plastic/PlasticRules.h>  // Get the value of the property. boolean propertyValue = plasticRules_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |