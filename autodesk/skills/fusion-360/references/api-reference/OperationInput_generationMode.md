# OperationInput.generationMode Property

Parent Object: [OperationInput](OperationInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/OperationInput.h>

## Description

Defines the automatic generation during the creation of the operation. Can be used to force or skip the generation of the new operation. By default the newly created operation will not be generated. The default value is SkipGeneration.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operationInput\_var" is a variable referencing an OperationInput object. |

"operationInput\_var" is a variable referencing an OperationInput object. ```` ``` #include <Cam/Operations/OperationInput.h>  // Get the value of the property. AutomaticGenerationModes propertyValue = operationInput_var->generationMode();  // Set the value of the property, where value_var is an AutomaticGenerationModes. bool returnValue = operationInput_var->generationMode(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [AutomaticGenerationModes](AutomaticGenerationModes.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |