# SetupChangeEventArgs.setup Property

Parent Object: [SetupChangeEventArgs](SetupChangeEventArgs.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupChangeEventArgs.h>

## Description

Provides access to the setup. Can be null in the case where the event is fired before the setup has been created or after it has been deleted.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupChangeEventArgs\_var" is a variable referencing a SetupChangeEventArgs object. |

"setupChangeEventArgs\_var" is a variable referencing a SetupChangeEventArgs object. ```` ``` #include <Cam/CAM/SetupChangeEventArgs.h>  // Get the value of the property. Ptr<Setup> propertyValue = setupChangeEventArgs_var->setup(); ``` ```` |

## Property Value

This is a read only property whose value is a [Setup](Setup.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |