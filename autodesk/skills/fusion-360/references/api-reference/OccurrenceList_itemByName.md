# OccurrenceList.itemByName Method

Parent Object: [OccurrenceList](OccurrenceList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/OccurrenceList.h>

## Description

Returns the specified occurrence using the name of the occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrenceList\_var" is a variable referencing an [OccurrenceList](OccurrenceList.htm) object.```` ``` returnValue = occurrenceList_var.itemByName(name) ``` ```` |

"occurrenceList\_var" is a variable referencing an [OccurrenceList](OccurrenceList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Occurrence](Occurrence.htm) | Returns the occurrence or null if an invalid name was specified |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the occurrence to return. |

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |