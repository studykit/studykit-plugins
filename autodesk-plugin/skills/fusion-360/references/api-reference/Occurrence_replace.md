# Occurrence.replace Method

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

Replaces this occurrence or all occurrences that reference the same external component with a new component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an [Occurrence](Occurrence.htm) object.```` ``` returnValue = occurrence_var.replace(newFile, replaceAll) ``` ```` |

"occurrence\_var" is a variable referencing an [Occurrence](Occurrence.htm) object.  ```` ``` #include <Fusion/Components/Occurrence.h>  returnValue = occurrence_var->replace(newFile, replaceAll); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the replacement was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| newFile | [DataFile](DataFile.htm) | Specifies the DataFile you want to use as the replacement. The DataFile specified must exist in the same hub as the parent assembly. |
| replaceAll | boolean | Indicates if you want to replace only this single occurrence or all occurrences that reference the same external design. |

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |