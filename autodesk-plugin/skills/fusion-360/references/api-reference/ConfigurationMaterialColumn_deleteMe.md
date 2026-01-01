# ConfigurationMaterialColumn.deleteMe Method

Parent Object: [ConfigurationMaterialColumn](ConfigurationMaterialColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialColumn.h>

## Description

Deletes this column from the table. Property columns cannot be deleted. If the table was obtained from a DataFile, this method will fail.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationMaterialColumn\_var" is a variable referencing a [ConfigurationMaterialColumn](ConfigurationMaterialColumn.htm) object.```` ``` returnValue = configurationMaterialColumn_var.deleteMe() ``` ```` |

"configurationMaterialColumn\_var" is a variable referencing a [ConfigurationMaterialColumn](ConfigurationMaterialColumn.htm) object. |

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