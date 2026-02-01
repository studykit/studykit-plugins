# CAMPatterns.itemByOperationId Method

Parent Object: [CAMPatterns](CAMPatterns.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMPatterns.h>

## Description

Returns the pattern with the specified operation id.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMPatterns\_var" is a variable referencing a [CAMPatterns](CAMPatterns.htm) object.```` ``` returnValue = cAMPatterns_var.itemByOperationId(id) ``` ```` |

"cAMPatterns\_var" is a variable referencing a [CAMPatterns](CAMPatterns.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CAMPattern](CAMPattern.htm) | Returns the specified pattern or null in the case where there is no pattern with the specified operation id. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | integer | The id of the pattern. |

## Version

Introduced in version May 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |