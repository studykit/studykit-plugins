# Design.designPlasticRules Property

Parent Object: [Design](Design.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Design.h>

## Description

Gets the collection of plastic rules in the design.

## Syntax

* [Python](#Python)
* [C++](#C++)

"design\_var" is a variable referencing a Design object. |

"design\_var" is a variable referencing a Design object. ```` ``` #include <Fusion/Fusion/Design.h>  // Get the value of the property. Ptr<PlasticRules> propertyValue = design_var->designPlasticRules(); ``` ```` |

## Property Value

This is a read only property whose value is a [PlasticRules](PlasticRules.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |