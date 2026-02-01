# ApplicationEventArgs.isValid Property

Parent Object: [ApplicationEventArgs](ApplicationEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ApplicationEventArgs.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationEventArgs\_var" is a variable referencing an ApplicationEventArgs object. |

"applicationEventArgs\_var" is a variable referencing an ApplicationEventArgs object. ```` ``` #include <Core/Application/ApplicationEventArgs.h>  // Get the value of the property. boolean propertyValue = applicationEventArgs_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |