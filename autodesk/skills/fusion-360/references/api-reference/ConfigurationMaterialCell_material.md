# ConfigurationMaterialCell.material Property

Parent Object: [ConfigurationMaterialCell](ConfigurationMaterialCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialCell.h>

## Description

Gets and sets the material associated with this cell. When setting this property, the material used must exist in the design.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationMaterialCell\_var" is a variable referencing a ConfigurationMaterialCell object. |

"configurationMaterialCell\_var" is a variable referencing a ConfigurationMaterialCell object. ```` ``` #include <Fusion/Configurations/ConfigurationMaterialCell.h>  // Get the value of the property. Ptr<Material> propertyValue = configurationMaterialCell_var->material();  // Set the value of the property, where value_var is a Material. bool returnValue = configurationMaterialCell_var->material(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Material](Material.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |