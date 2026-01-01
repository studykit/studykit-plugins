# Occurrences.addFromConfiguration Method

Parent Object: [Occurrences](Occurrences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrences.h>

## Description

Method that inserts a configuration from a configured design. The insert will fail if the configured design being used is not from the same project as the file it is being inserted into.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrences\_var" is a variable referencing an [Occurrences](Occurrences.htm) object.```` ``` returnValue = occurrences_var.addFromConfiguration(configurationRow, transform) ``` ```` |

"occurrences\_var" is a variable referencing an [Occurrences](Occurrences.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Occurrence](Occurrence.htm) | Returns the newly created occurrence or null if the add failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| configurationRow | [ConfigurationRow](ConfigurationRow.htm) | The row that specifies which configuration to use. |
| transform | [Matrix3D](Matrix3D.htm) | A transform that defines the location for the new occurrence. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |