# SetupInput.objectType Property

Parent Object: [SetupInput](SetupInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupInput\_var" is a variable referencing a SetupInput object.  ```` ``` # Get the value of the property. propertyValue = setupInput_var.objectType ``` ```` |

"setupInput\_var" is a variable referencing a SetupInput object. ```` ``` #include <Cam/CAM/SetupInput.h>  // Get the value of the property. string propertyValue = setupInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |