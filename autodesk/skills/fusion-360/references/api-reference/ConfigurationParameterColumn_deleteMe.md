# ConfigurationParameterColumn.deleteMe Method

Parent Object: [ConfigurationParameterColumn](ConfigurationParameterColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationParameterColumn.h>

## Description

Deletes this column from the table. Property columns cannot be deleted. If the table was obtained from a DataFile, this method will fail.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationParameterColumn\_var" is a variable referencing a [ConfigurationParameterColumn](ConfigurationParameterColumn.htm) object.```` ``` returnValue = configurationParameterColumn_var.deleteMe() ``` ```` |

"configurationParameterColumn\_var" is a variable referencing a [ConfigurationParameterColumn](ConfigurationParameterColumn.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the deletion was successful. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |