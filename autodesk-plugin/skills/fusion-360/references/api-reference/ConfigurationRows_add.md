# ConfigurationRows.add Method

Parent Object: [ConfigurationRows](ConfigurationRows.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationRows.h>

## Description

Adds a new row to the table. For the top table, this creates a new configuration. For theme tables, this creates a new theme. The new row is added to the bottom of the table, and the cell values are copied from the row above it. You can also use the ConfigurationRow.copy method to create a new row by copying any existing row.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationRows\_var" is a variable referencing a [ConfigurationRows](ConfigurationRows.htm) object.```` ``` returnValue = configurationRows_var.add(name) ``` ```` |

"configurationRows\_var" is a variable referencing a [ConfigurationRows](ConfigurationRows.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationRow](ConfigurationRow.htm) | Returns the newly created row. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the new row. An empty string can be provided, which will cause Fusion to use a default naming scheme to create a name. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |