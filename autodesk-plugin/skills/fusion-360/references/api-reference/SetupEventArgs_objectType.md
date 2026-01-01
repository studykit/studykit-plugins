# SetupEventArgs.objectType Property

Parent Object: [SetupEventArgs](SetupEventArgs.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupEventArgs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupEventArgs\_var" is a variable referencing a SetupEventArgs object.  ```` ``` # Get the value of the property. propertyValue = setupEventArgs_var.objectType ``` ```` |

"setupEventArgs\_var" is a variable referencing a SetupEventArgs object. ```` ``` #include <Cam/CAM/SetupEventArgs.h>  // Get the value of the property. string propertyValue = setupEventArgs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |