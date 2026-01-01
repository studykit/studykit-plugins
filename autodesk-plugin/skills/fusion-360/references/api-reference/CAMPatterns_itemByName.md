# CAMPatterns.itemByName Method

Parent Object: [CAMPatterns](CAMPatterns.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMPatterns.h>

## Description

Returns the pattern with the specified name (as appears in the browser).

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMPatterns\_var" is a variable referencing a [CAMPatterns](CAMPatterns.htm) object.```` ``` returnValue = cAMPatterns_var.itemByName(name) ``` ```` |

"cAMPatterns\_var" is a variable referencing a [CAMPatterns](CAMPatterns.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CAMPattern](CAMPattern.htm) | Returns the specified pattern or null in the case where there is no pattern with the specified name. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name (as it appears in the browser) of the pattern. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |