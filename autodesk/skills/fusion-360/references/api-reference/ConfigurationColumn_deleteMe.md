# ConfigurationColumn.deleteMe Method

Parent Object: [ConfigurationColumn](ConfigurationColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationColumn.h>

## Description

Deletes this column from the table. Property columns cannot be deleted. If the table was obtained from a DataFile, this method will fail.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationColumn\_var" is a variable referencing a [ConfigurationColumn](ConfigurationColumn.htm) object.```` ``` returnValue = configurationColumn_var.deleteMe() ``` ```` |

"configurationColumn\_var" is a variable referencing a [ConfigurationColumn](ConfigurationColumn.htm) object. |

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