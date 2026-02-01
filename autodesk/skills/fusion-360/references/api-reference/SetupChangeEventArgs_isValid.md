# SetupChangeEventArgs.isValid Property

Parent Object: [SetupChangeEventArgs](SetupChangeEventArgs.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupChangeEventArgs.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupChangeEventArgs\_var" is a variable referencing a SetupChangeEventArgs object. |

"setupChangeEventArgs\_var" is a variable referencing a SetupChangeEventArgs object. ```` ``` #include <Cam/CAM/SetupChangeEventArgs.h>  // Get the value of the property. boolean propertyValue = setupChangeEventArgs_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |