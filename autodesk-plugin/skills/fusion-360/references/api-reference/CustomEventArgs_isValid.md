# CustomEventArgs.isValid Property

Parent Object: [CustomEventArgs](CustomEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/CustomEventArgs.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customEventArgs\_var" is a variable referencing a CustomEventArgs object. |

"customEventArgs\_var" is a variable referencing a CustomEventArgs object. ```` ``` #include <Core/Application/CustomEventArgs.h>  // Get the value of the property. boolean propertyValue = customEventArgs_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |