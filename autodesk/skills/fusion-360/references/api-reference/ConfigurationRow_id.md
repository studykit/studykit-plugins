# ConfigurationRow.id Property

Parent Object: [ConfigurationRow](ConfigurationRow.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationRow.h>

## Description

Gets the unique ID that identifies this row. The ID remains constant for this row as long as the row exists. This is different than the name, which the user can change.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationRow\_var" is a variable referencing a ConfigurationRow object. |

"configurationRow\_var" is a variable referencing a ConfigurationRow object. ```` ``` #include <Fusion/Configurations/ConfigurationRow.h>  // Get the value of the property. string propertyValue = configurationRow_var->id(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |