# ConfigurationRow.generate Method

Parent Object: [ConfigurationRow](ConfigurationRow.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationRow.h>

## Description

Causes this row to be generated.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationRow\_var" is a variable referencing a [ConfigurationRow](ConfigurationRow.htm) object.```` ``` returnValue = configurationRow_var.generate() ``` ```` |

"configurationRow\_var" is a variable referencing a [ConfigurationRow](ConfigurationRow.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationFuture](ConfigurationFuture.htm) | Returns a future that can be used to determine when the generation is complete. Null is returned in the case where starting the generation fails. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |