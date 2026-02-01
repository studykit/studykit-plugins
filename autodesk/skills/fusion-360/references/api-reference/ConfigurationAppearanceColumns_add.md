# ConfigurationAppearanceColumns.add Method

Parent Object: [ConfigurationAppearanceColumns](ConfigurationAppearanceColumns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationAppearanceColumns.h>

## Description

Adds a new column to the appearance table. If you are adding the first column to the table and it is anything other than the root component, an additional column for the root component will automatically be created as the first column.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationAppearanceColumns\_var" is a variable referencing a [ConfigurationAppearanceColumns](ConfigurationAppearanceColumns.htm) object.```` ``` returnValue = configurationAppearanceColumns_var.add(entity) ``` ```` |

"configurationAppearanceColumns\_var" is a variable referencing a [ConfigurationAppearanceColumns](ConfigurationAppearanceColumns.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationAppearanceColumn](ConfigurationAppearanceColumn.htm) | Returns the newly created ConfigurationAppearanceColumn object or null if it fails. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| entity | [Base](Base.htm) | The root component, occurrence, or body whose appearance will be controlled by this column. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |