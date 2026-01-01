# ConfigurationInsertColumn.deleteMe Method

Parent Object: [ConfigurationInsertColumn](ConfigurationInsertColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationInsertColumn.h>

## Description

Deletes this column from the table. Property columns cannot be deleted. If the table was obtained from a DataFile, this method will fail.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationInsertColumn\_var" is a variable referencing a [ConfigurationInsertColumn](ConfigurationInsertColumn.htm) object.```` ``` returnValue = configurationInsertColumn_var.deleteMe() ``` ```` |

"configurationInsertColumn\_var" is a variable referencing a [ConfigurationInsertColumn](ConfigurationInsertColumn.htm) object. |

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