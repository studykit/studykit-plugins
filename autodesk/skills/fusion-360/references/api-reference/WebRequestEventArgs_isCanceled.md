# WebRequestEventArgs.isCanceled Property

Parent Object: [WebRequestEventArgs](WebRequestEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/WebRequestEventArgs.h>

## Description

Used during the insertingFromURL and openingFromURL events to get or set if the insert or open should be allowed to continue. This defaults to false, which will allow the operation to continue as normal. This property should be ignored for all events besides the insertingFromURL and openingFromURL events.

## Syntax

* [Python](#Python)
* [C++](#C++)

"webRequestEventArgs\_var" is a variable referencing a WebRequestEventArgs object. |

"webRequestEventArgs\_var" is a variable referencing a WebRequestEventArgs object. ```` ``` #include <Core/Application/WebRequestEventArgs.h>  // Get the value of the property. boolean propertyValue = webRequestEventArgs_var->isCanceled();  // Set the value of the property, where value_var is a boolean. bool returnValue = webRequestEventArgs_var->isCanceled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |