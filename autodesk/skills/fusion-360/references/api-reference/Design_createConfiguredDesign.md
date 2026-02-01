# Design.createConfiguredDesign Method

Parent Object: [Design](Design.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Design.h>

## Description

Converts this design into a configured design. The returned ConfigurationTable has a single row and no columns. You can use it to add columns and rows to define the configuration.

## Syntax

* [Python](#Python)
* [C++](#C++)

"design\_var" is a variable referencing a [Design](Design.htm) object.```` ``` returnValue = design_var.createConfiguredDesign() ``` ```` |

"design\_var" is a variable referencing a [Design](Design.htm) object. |

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