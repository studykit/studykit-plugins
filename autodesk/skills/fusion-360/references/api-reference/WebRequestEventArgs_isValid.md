# WebRequestEventArgs.isValid Property

Parent Object: [WebRequestEventArgs](WebRequestEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/WebRequestEventArgs.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"webRequestEventArgs\_var" is a variable referencing a WebRequestEventArgs object. |

"webRequestEventArgs\_var" is a variable referencing a WebRequestEventArgs object. ```` ``` #include <Core/Application/WebRequestEventArgs.h>  // Get the value of the property. boolean propertyValue = webRequestEventArgs_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |