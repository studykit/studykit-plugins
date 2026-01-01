# ConfigurationRows.itemById Method

Parent Object: [ConfigurationRows](ConfigurationRows.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationRows.h>

## Description

A method that returns the row with the specified ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationRows\_var" is a variable referencing a [ConfigurationRows](ConfigurationRows.htm) object.```` ``` returnValue = configurationRows_var.itemById(id) ``` ```` |

"configurationRows\_var" is a variable referencing a [ConfigurationRows](ConfigurationRows.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationRow](ConfigurationRow.htm) | Returns the specified row or null if a row with the specified ID does not exist. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The id of the row to return. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |