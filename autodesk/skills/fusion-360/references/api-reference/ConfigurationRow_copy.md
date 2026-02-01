# ConfigurationRow.copy Method

Parent Object: [ConfigurationRow](ConfigurationRow.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationRow.h>

## Description

Creates a new row by copying this row.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationRow\_var" is a variable referencing a [ConfigurationRow](ConfigurationRow.htm) object.```` ``` returnValue = configurationRow_var.copy(name) ``` ```` |

"configurationRow\_var" is a variable referencing a [ConfigurationRow](ConfigurationRow.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationRow](ConfigurationRow.htm) | Returns the newly created row or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name to use for the new row. An empty string indicates that Fusion should use the default naming scheme.   Names must be unique with respect to other rows in this table. If you specify a name that exists, Fusion will append a counter to ensure uniqueness. For example, if "Small" is already used and you name another row "Small", you will end up with "Small (1)". |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |