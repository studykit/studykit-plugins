# URL.parent Property

Parent Object: [URL](URL.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/URL.h>

## Description

Get the parent URL, represented by the section before the last '/'.

## Syntax

* [Python](#Python)
* [C++](#C++)

"uRL\_var" is a variable referencing a URL object. |

"uRL\_var" is a variable referencing a URL object. ```` ``` #include <Core/Application/URL.h>  // Get the value of the property. Ptr<URL> propertyValue = uRL_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [URL](URL.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |