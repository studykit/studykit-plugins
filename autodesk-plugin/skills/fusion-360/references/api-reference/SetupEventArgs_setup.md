# SetupEventArgs.setup Property

Parent Object: [SetupEventArgs](SetupEventArgs.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupEventArgs.h>

## Description

Provides access to the setup. Can be null in the case where the event is fired before the setup has been created or after it has been deleted.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupEventArgs\_var" is a variable referencing a SetupEventArgs object. |

"setupEventArgs\_var" is a variable referencing a SetupEventArgs object. ```` ``` #include <Cam/CAM/SetupEventArgs.h>  // Get the value of the property. Ptr<Setup> propertyValue = setupEventArgs_var->setup(); ``` ```` |

## Property Value

This is a read only property whose value is a [Setup](Setup.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |