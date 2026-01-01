# ConfigurationCustomThemeTable.deleteMe Method

Parent Object: [ConfigurationCustomThemeTable](ConfigurationCustomThemeTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationCustomThemeTable.h>

## Description

Deletes this custom theme table from the configuration.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationCustomThemeTable\_var" is a variable referencing a [ConfigurationCustomThemeTable](ConfigurationCustomThemeTable.htm) object.```` ``` returnValue = configurationCustomThemeTable_var.deleteMe(deleteColumns) ``` ```` |

"configurationCustomThemeTable\_var" is a variable referencing a [ConfigurationCustomThemeTable](ConfigurationCustomThemeTable.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the delete was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| deleteColumns | boolean | If true, this deletes the columns in the custom theme table. If false, it moves them back to the top table. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |