# WebRequestEventArgs.id Property

Parent Object: [WebRequestEventArgs](WebRequestEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/WebRequestEventArgs.h>

## Description

Returns the value specified as the "id" parameter in the URL. This will be decoded. It can be an empty string if the "id" parameter was not specified in the URL.

## Syntax

* [Python](#Python)
* [C++](#C++)

"webRequestEventArgs\_var" is a variable referencing a WebRequestEventArgs object. |

"webRequestEventArgs\_var" is a variable referencing a WebRequestEventArgs object. ```` ``` #include <Core/Application/WebRequestEventArgs.h>  // Get the value of the property. string propertyValue = webRequestEventArgs_var->id(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |