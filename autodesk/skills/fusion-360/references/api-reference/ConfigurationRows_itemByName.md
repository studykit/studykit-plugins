# ConfigurationRows.itemByName Method

Parent Object: [ConfigurationRows](ConfigurationRows.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationRows.h>

## Description

A method that returns the row with the specified name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationRows\_var" is a variable referencing a [ConfigurationRows](ConfigurationRows.htm) object.```` ``` returnValue = configurationRows_var.itemByName(name) ``` ```` |

"configurationRows\_var" is a variable referencing a [ConfigurationRows](ConfigurationRows.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationRow](ConfigurationRow.htm) | Returns the specified row or null if the named row does not exist. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the row to return. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |