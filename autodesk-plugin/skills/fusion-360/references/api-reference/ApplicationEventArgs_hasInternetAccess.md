# ApplicationEventArgs.hasInternetAccess Property

Parent Object: [ApplicationEventArgs](ApplicationEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ApplicationEventArgs.h>

## Description

Gets if the client computer has access to the Internet.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationEventArgs\_var" is a variable referencing an ApplicationEventArgs object. |

"applicationEventArgs\_var" is a variable referencing an ApplicationEventArgs object. ```` ``` #include <Core/Application/ApplicationEventArgs.h>  // Get the value of the property. boolean propertyValue = applicationEventArgs_var->hasInternetAccess(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |