# ConfigurationColumns.addSuppressColumn Method

Parent Object: [ConfigurationColumns](ConfigurationColumns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationColumns.h>

## Description

Adds a new column to control the suppression of a feature. The term "feature" is used broadly and includes anything displayed in the timeline. If a suppression column already exists for the feature, the existing column is returned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationColumns\_var" is a variable referencing a [ConfigurationColumns](ConfigurationColumns.htm) object.```` ``` returnValue = configurationColumns_var.addSuppressColumn(feature) ``` ```` |

"configurationColumns\_var" is a variable referencing a [ConfigurationColumns](ConfigurationColumns.htm) object.  ```` ``` #include <Fusion/Configurations/ConfigurationColumns.h>  returnValue = configurationColumns_var->addSuppressColumn(feature); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationSuppressColumn](ConfigurationSuppressColumn.htm) | Returns the new column or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| feature | [Base](Base.htm) | The feature to add to the table. Any object that is displayed in the timeline can be used as input. For example, some valid objects are any modeling features, sketches, construction geometry, and joints. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |