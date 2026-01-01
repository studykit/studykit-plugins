# ConfigurationRows.item Method

Parent Object: [ConfigurationRows](ConfigurationRows.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationRows.h>

## Description

A method that returns the specified row using an index into the collection. These are returned in the same order as in the table; the first row is the default row.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationRows\_var" is a variable referencing a [ConfigurationRows](ConfigurationRows.htm) object.```` ``` returnValue = configurationRows_var.item(index) ``` ```` |

"configurationRows\_var" is a variable referencing a [ConfigurationRows](ConfigurationRows.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationRow](ConfigurationRow.htm) | Returns the specified row or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the row to return, where the first row is index 0. The headers do not count as a row. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |