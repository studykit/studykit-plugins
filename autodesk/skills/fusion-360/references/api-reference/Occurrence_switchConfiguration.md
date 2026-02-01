# Occurrence.switchConfiguration Method

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

Changes which configuration is used for this occurrence. Use the isConfiguration property to determine if this occurrence references a configuration.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an [Occurrence](Occurrence.htm) object.```` ``` returnValue = occurrence_var.switchConfiguration(newRow) ``` ```` |

"occurrence\_var" is a variable referencing an [Occurrence](Occurrence.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the switch was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| newRow | [ConfigurationRow](ConfigurationRow.htm) | The row to switch to. This row must be from the same ConfigurationTopTable as the current row. You can access the table from the parent design. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |