# ConfigurationVisibilityCell.isVisible Property

Parent Object: [ConfigurationVisibilityCell](ConfigurationVisibilityCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationVisibilityCell.h>

## Description

Specifies if the entity is visible or not. This property behaves as read-only when the table is obtained from a DataFile.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationVisibilityCell\_var" is a variable referencing a ConfigurationVisibilityCell object. |

"configurationVisibilityCell\_var" is a variable referencing a ConfigurationVisibilityCell object. ```` ``` #include <Fusion/Configurations/ConfigurationVisibilityCell.h>  // Get the value of the property. boolean propertyValue = configurationVisibilityCell_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = configurationVisibilityCell_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |