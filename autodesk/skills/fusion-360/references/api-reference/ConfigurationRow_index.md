# ConfigurationRow.index Property

Parent Object: [ConfigurationRow](ConfigurationRow.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationRow.h>

## Description

The index position of this row within the table. The first row is at index 0 and does not include the header row.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationRow\_var" is a variable referencing a ConfigurationRow object. |

"configurationRow\_var" is a variable referencing a ConfigurationRow object. ```` ``` #include <Fusion/Configurations/ConfigurationRow.h>  // Get the value of the property. uinteger propertyValue = configurationRow_var->index(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |