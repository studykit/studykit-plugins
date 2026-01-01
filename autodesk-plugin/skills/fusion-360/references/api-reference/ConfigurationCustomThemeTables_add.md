# ConfigurationCustomThemeTables.add Method

Parent Object: [ConfigurationCustomThemeTables](ConfigurationCustomThemeTables.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationCustomThemeTables.h>

## Description

Creates a new custom theme table using the specified columns.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationCustomThemeTables\_var" is a variable referencing a [ConfigurationCustomThemeTables](ConfigurationCustomThemeTables.htm) object.```` ``` returnValue = configurationCustomThemeTables_var.add(columns) ``` ```` |

"configurationCustomThemeTables\_var" is a variable referencing a [ConfigurationCustomThemeTables](ConfigurationCustomThemeTables.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationCustomThemeTable](ConfigurationCustomThemeTable.htm) | Returns the newly created ConfigurationCustomThemeTable or null if the creation fails. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| columns | ConfigurationColumn[] | An array of ConfigurationColumn objects used to create a new custom theme table. The columns must exist within the top configuration table, and they cannot include any ConfigurationThemeColumn, ConfigurationPropertyColumn, ConfigurationAppearanceColumn, ConfigurationMaterialColumn, ConfigurationPlasticRuleColumn, or ConfigurationSheetMetalRuleColumn objects. The specified columns will be removed from the main table, and a new ConfigurationThemeColumn will be created in the top table to reference the newly created custom theme table. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |