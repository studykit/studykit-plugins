# ConfigurationJointSnapColumn.snaps Property

Parent Object: [ConfigurationJointSnapColumn](ConfigurationJointSnapColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationJointSnapColumn.h>

## Description

Provides access to any joint snaps that have been defined for this column. Using the returned collection you can define new joint snaps. Use the cell to specify which of the defined snaps is used for a specific row.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationJointSnapColumn\_var" is a variable referencing a ConfigurationJointSnapColumn object. |

"configurationJointSnapColumn\_var" is a variable referencing a ConfigurationJointSnapColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationJointSnapColumn.h>  // Get the value of the property. Ptr<ConfigurationJointSnaps> propertyValue = configurationJointSnapColumn_var->snaps(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationJointSnaps](ConfigurationJointSnaps.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |