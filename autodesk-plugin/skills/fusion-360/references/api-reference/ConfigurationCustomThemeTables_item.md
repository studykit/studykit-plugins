# ConfigurationCustomThemeTables.item Method

Parent Object: [ConfigurationCustomThemeTables](ConfigurationCustomThemeTables.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationCustomThemeTables.h>

## Description

A method that returns the specified custom theme table using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationCustomThemeTables\_var" is a variable referencing a [ConfigurationCustomThemeTables](ConfigurationCustomThemeTables.htm) object.```` ``` returnValue = configurationCustomThemeTables_var.item(index) ``` ```` |

"configurationCustomThemeTables\_var" is a variable referencing a [ConfigurationCustomThemeTables](ConfigurationCustomThemeTables.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationCustomThemeTable](ConfigurationCustomThemeTable.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |