# Application.getLastError Method

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

Returns information about the last error that occurred.

## Syntax

* [Python](#Python)
* [C++](#C++)

"application\_var" is a variable referencing an [Application](Application.htm) object. |

```` ```  #include <Core/Application/Application.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| integer | Returns the number of the specific error. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| description | string | A description of the last error in English.   This is an optional argument whose default value is "". |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |