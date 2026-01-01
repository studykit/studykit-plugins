# URL.join Method

Parent Object: [URL](URL.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/URL.h>

## Description

Join this URL with the given path and return the resulting URL. The operation does not alter the current URL. Join inserts a slash '/' to properly extend the path, so that "http://foo".join("bar") will return "http://foo/bar", not "http://foobar".

## Syntax

* [Python](#Python)
* [C++](#C++)

"uRL\_var" is a variable referencing a [URL](URL.htm) object.```` ``` returnValue = uRL_var.join(path) ``` ```` |

"uRL\_var" is a variable referencing a [URL](URL.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [URL](URL.htm) | Returns the joined URL. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| path | string | The path to join to this URL. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |