# HttpResponse.headers Method

Parent Object: [HttpResponse](HttpResponse.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpResponse.h>

## Description

Get the response headers.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpResponse\_var" is a variable referencing a [HttpResponse](HttpResponse.htm) object. |

```` ```  #include <Core/Application/HttpResponse.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true on success or false on error. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| names | string[] | An array of all the header key names. |
| values | string[] | An array of all the header values. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |