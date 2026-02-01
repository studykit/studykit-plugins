# SetupChangeEventArgs.info Property

Parent Object: [SetupChangeEventArgs](SetupChangeEventArgs.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupChangeEventArgs.h>

## Description

Provides access to an information string. The optional string may contain additional information about the change.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupChangeEventArgs\_var" is a variable referencing a SetupChangeEventArgs object. |

"setupChangeEventArgs\_var" is a variable referencing a SetupChangeEventArgs object. ```` ``` #include <Cam/CAM/SetupChangeEventArgs.h>  // Get the value of the property. string propertyValue = setupChangeEventArgs_var->info(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |