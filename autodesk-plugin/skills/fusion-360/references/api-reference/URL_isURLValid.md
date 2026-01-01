# URL.isURLValid Property

Parent Object: [URL](URL.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/URL.h>

## Description

Check whether the URL is valid. Ensures that the URL is formatted with a protocol followed by a path which can be empty. The check is independent of the existence of the resource the URL may point to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"uRL\_var" is a variable referencing a URL object. |

"uRL\_var" is a variable referencing a URL object. ```` ``` #include <Core/Application/URL.h>  // Get the value of the property. boolean propertyValue = uRL_var->isURLValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |