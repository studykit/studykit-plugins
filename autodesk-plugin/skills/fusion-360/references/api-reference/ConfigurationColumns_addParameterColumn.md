# ConfigurationColumns.addParameterColumn Method

Parent Object: [ConfigurationColumns](ConfigurationColumns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationColumns.h>

## Description

Adds a new parameter column to the configuration table. If a parameter column already exists for the parameter, the existing column is returned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationColumns\_var" is a variable referencing a [ConfigurationColumns](ConfigurationColumns.htm) object.```` ``` returnValue = configurationColumns_var.addParameterColumn(parameter) ``` ```` |

"configurationColumns\_var" is a variable referencing a [ConfigurationColumns](ConfigurationColumns.htm) object.  ```` ``` #include <Fusion/Configurations/ConfigurationColumns.h>  returnValue = configurationColumns_var->addParameterColumn(parameter); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationParameterColumn](ConfigurationParameterColumn.htm) | Returns the new column or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parameter | [Parameter](Parameter.htm) | The parameter to add to the table. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |