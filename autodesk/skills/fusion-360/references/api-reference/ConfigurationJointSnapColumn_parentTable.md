# ConfigurationJointSnapColumn.parentTable Property

Parent Object: [ConfigurationJointSnapColumn](ConfigurationJointSnapColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationJointSnapColumn.h>

## Description

This property returns the parent table, either the top or custom theme table this column is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationJointSnapColumn\_var" is a variable referencing a ConfigurationJointSnapColumn object. |

"configurationJointSnapColumn\_var" is a variable referencing a ConfigurationJointSnapColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationJointSnapColumn.h>  // Get the value of the property. Ptr<ConfigurationTable> propertyValue = configurationJointSnapColumn_var->parentTable(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationTable](ConfigurationTable.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |