# HttpRequest.execute Method

Parent Object: [HttpRequest](HttpRequest.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpRequest.h>

## Description

Execute this request asynchronously. The response will be sent to the completed event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpRequest\_var" is a variable referencing a [HttpRequest](HttpRequest.htm) object.```` ``` returnValue = httpRequest_var.execute() ``` ```` |

"httpRequest\_var" is a variable referencing a [HttpRequest](HttpRequest.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the request was successfully started. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |