# NCProgramPostProcessOptions.objectType Property

Parent Object: [NCProgramPostProcessOptions](NCProgramPostProcessOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCProgramPostProcessOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCProgramPostProcessOptions\_var" is a variable referencing a NCProgramPostProcessOptions object.  ```` ``` # Get the value of the property. propertyValue = nCProgramPostProcessOptions_var.objectType ``` ```` |

"nCProgramPostProcessOptions\_var" is a variable referencing a NCProgramPostProcessOptions object. ```` ``` #include <Cam/NCProgram/NCProgramPostProcessOptions.h>  // Get the value of the property. string propertyValue = nCProgramPostProcessOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |