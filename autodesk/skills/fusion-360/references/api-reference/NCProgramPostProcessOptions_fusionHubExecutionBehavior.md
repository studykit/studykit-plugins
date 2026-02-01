# NCProgramPostProcessOptions.fusionHubExecutionBehavior Property

Parent Object: [NCProgramPostProcessOptions](NCProgramPostProcessOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCProgramPostProcessOptions.h>

## Description

Gets and sets the post process behavior for exporting to Fusion Hub. Uses fusionHubExecutionBehavior\_ExportWithRelationship by default.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCProgramPostProcessOptions\_var" is a variable referencing a NCProgramPostProcessOptions object. |

"nCProgramPostProcessOptions\_var" is a variable referencing a NCProgramPostProcessOptions object. ```` ``` #include <Cam/NCProgram/NCProgramPostProcessOptions.h>  // Get the value of the property. FusionHubExecutionBehaviors propertyValue = nCProgramPostProcessOptions_var->fusionHubExecutionBehavior();  // Set the value of the property, where value_var is a FusionHubExecutionBehaviors. bool returnValue = nCProgramPostProcessOptions_var->fusionHubExecutionBehavior(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [FusionHubExecutionBehaviors](FusionHubExecutionBehaviors.htm).

## Version

Introduced in version July 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |