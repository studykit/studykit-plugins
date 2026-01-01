# ConfigurationPropertyColumn.deleteMe Method

Parent Object: [ConfigurationPropertyColumn](ConfigurationPropertyColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationPropertyColumn.h>

## Description

Deletes this column from the table. Property columns cannot be deleted. If the table was obtained from a DataFile, this method will fail.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationPropertyColumn\_var" is a variable referencing a [ConfigurationPropertyColumn](ConfigurationPropertyColumn.htm) object.```` ``` returnValue = configurationPropertyColumn_var.deleteMe() ``` ```` |

"configurationPropertyColumn\_var" is a variable referencing a [ConfigurationPropertyColumn](ConfigurationPropertyColumn.htm) object. |

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