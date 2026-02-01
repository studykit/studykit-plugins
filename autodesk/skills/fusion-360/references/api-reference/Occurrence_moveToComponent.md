# Occurrence.moveToComponent Method

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

Moves this occurrence from it's current component into the component owned by the specified occurrence. This occurrence and the target occurrence must be in the same context.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an [Occurrence](Occurrence.htm) object.```` ``` returnValue = occurrence_var.moveToComponent(targetOccurrence) ``` ```` |

"occurrence\_var" is a variable referencing an [Occurrence](Occurrence.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Occurrence](Occurrence.htm) | Returns the moved Occurrence or null in the case the move failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| targetOccurrence | [Occurrence](Occurrence.htm) | The target occurrence defines both the component and the transform to apply when moving the occurrence. The occurrence will be copied into the parent component of the target occurrence and the target occurrence also defines the transform of how the occurrence will be copied so that the occurrence maintains it's same position in model space. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |