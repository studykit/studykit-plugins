# PlasticRule.units Property

Parent Object: [PlasticRule](PlasticRule.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/PlasticRule.h>

## Description

Gets the units this rule uses to display values in the dialog. Rules currently only use mm or inch and the units are permanently associated with a rule and cannot be modified.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plasticRule\_var" is a variable referencing a PlasticRule object. |

"plasticRule\_var" is a variable referencing a PlasticRule object. ```` ``` #include <Fusion/Plastic/PlasticRule.h>  // Get the value of the property. string propertyValue = plasticRule_var->units(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |