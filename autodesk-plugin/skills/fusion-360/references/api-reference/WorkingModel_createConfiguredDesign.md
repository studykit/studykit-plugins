# WorkingModel.createConfiguredDesign Method

Parent Object: [WorkingModel](WorkingModel.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/WorkingModel.h>

## Description

Converts this design into a configured design. The returned ConfigurationTable has a single row and no columns. You can use it to add columns and rows to define the configuration.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workingModel\_var" is a variable referencing a [WorkingModel](WorkingModel.htm) object.```` ``` returnValue = workingModel_var.createConfiguredDesign() ``` ```` |

"workingModel\_var" is a variable referencing a [WorkingModel](WorkingModel.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationTopTable](ConfigurationTopTable.htm) | Returns the ConfigurationTable that defines the configurations for this design. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |