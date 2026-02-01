# EventArgs.isValid Property

Parent Object: [EventArgs](EventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/EventArgs.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"eventArgs\_var" is a variable referencing an EventArgs object. |

"eventArgs\_var" is a variable referencing an EventArgs object. ```` ``` #include <Core/Application/EventArgs.h>  // Get the value of the property. boolean propertyValue = eventArgs_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |