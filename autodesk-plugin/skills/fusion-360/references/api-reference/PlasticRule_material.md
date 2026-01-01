# PlasticRule.material Property

Parent Object: [PlasticRule](PlasticRule.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/PlasticRule.h>

## Description

Gets and sets the material assigned to this plastic rule

## Syntax

* [Python](#Python)
* [C++](#C++)

"plasticRule\_var" is a variable referencing a PlasticRule object. |

"plasticRule\_var" is a variable referencing a PlasticRule object. ```` ``` #include <Fusion/Plastic/PlasticRule.h>  // Get the value of the property. Ptr<Material> propertyValue = plasticRule_var->material();  // Set the value of the property, where value_var is a Material. bool returnValue = plasticRule_var->material(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Material](Material.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |