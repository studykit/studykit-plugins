# ConfigurationSuppressCell.isSuppressed Property

Parent Object: [ConfigurationSuppressCell](ConfigurationSuppressCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationSuppressCell.h>

## Description

Specifies if the feature is suppressed or not. This property behaves as read-only when the table is obtained from a DataFile.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationSuppressCell\_var" is a variable referencing a ConfigurationSuppressCell object. |

"configurationSuppressCell\_var" is a variable referencing a ConfigurationSuppressCell object. ```` ``` #include <Fusion/Configurations/ConfigurationSuppressCell.h>  // Get the value of the property. boolean propertyValue = configurationSuppressCell_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = configurationSuppressCell_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |