# NCProgramPostProcessOptions.postProcessExecutionBehavior Property

Parent Object: [NCProgramPostProcessOptions](NCProgramPostProcessOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCProgramPostProcessOptions.h>

## Description

Gets and sets the post process behavior with regards to the operations' error or out of date states. Uses PostProcessExecutionBehavior\_OmitInvalidAndEmptyOperations by default.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCProgramPostProcessOptions\_var" is a variable referencing a NCProgramPostProcessOptions object. |

"nCProgramPostProcessOptions\_var" is a variable referencing a NCProgramPostProcessOptions object. ```` ``` #include <Cam/NCProgram/NCProgramPostProcessOptions.h>  // Get the value of the property. PostProcessExecutionBehaviors propertyValue = nCProgramPostProcessOptions_var->postProcessExecutionBehavior();  // Set the value of the property, where value_var is a PostProcessExecutionBehaviors. bool returnValue = nCProgramPostProcessOptions_var->postProcessExecutionBehavior(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PostProcessExecutionBehaviors](PostProcessExecutionBehaviors.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |