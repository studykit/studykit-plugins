# URL.pathName Property

Parent Object: [URL](URL.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/URL.h>

## Description

Get the path name of the URL, including the last '/' of the protocol followed by the path of the URL.

## Syntax

* [Python](#Python)
* [C++](#C++)

"uRL\_var" is a variable referencing a URL object. |

"uRL\_var" is a variable referencing a URL object. ```` ``` #include <Core/Application/URL.h>  // Get the value of the property. string propertyValue = uRL_var->pathName(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |