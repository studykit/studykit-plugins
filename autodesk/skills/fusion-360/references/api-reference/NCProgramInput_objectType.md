# NCProgramInput.objectType Property

Parent Object: [NCProgramInput](NCProgramInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCProgramInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCProgramInput\_var" is a variable referencing a NCProgramInput object.  ```` ``` # Get the value of the property. propertyValue = nCProgramInput_var.objectType ``` ```` |

"nCProgramInput\_var" is a variable referencing a NCProgramInput object. ```` ``` #include <Cam/NCProgram/NCProgramInput.h>  // Get the value of the property. string propertyValue = nCProgramInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |