# NCProgramPostProcessOptions.isFailOnToolNumberDuplication Property

Parent Object: [NCProgramPostProcessOptions](NCProgramPostProcessOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCProgramPostProcessOptions.h>

## Description

Toggles whether the post processing should abort if two tools with the same tool number have been detected. True by default. If true, an exception will be thrown if at least two tools map to the same tool number. If false, the post processor will not perform a tool change if the tool number is the same, which may mean that the wrong tool is used for an operation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCProgramPostProcessOptions\_var" is a variable referencing a NCProgramPostProcessOptions object. |

"nCProgramPostProcessOptions\_var" is a variable referencing a NCProgramPostProcessOptions object. ```` ``` #include <Cam/NCProgram/NCProgramPostProcessOptions.h>  // Get the value of the property. boolean propertyValue = nCProgramPostProcessOptions_var->isFailOnToolNumberDuplication();  // Set the value of the property, where value_var is a boolean. bool returnValue = nCProgramPostProcessOptions_var->isFailOnToolNumberDuplication(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |