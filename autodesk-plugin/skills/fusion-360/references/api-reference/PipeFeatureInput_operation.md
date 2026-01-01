# PipeFeatureInput.operation Property

Parent Object: [PipeFeatureInput](PipeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeatureInput.h>

## Description

Gets and sets the type of operation performed by the Pipe.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeatureInput\_var" is a variable referencing a PipeFeatureInput object. |

"pipeFeatureInput\_var" is a variable referencing a PipeFeatureInput object. ```` ``` #include <Fusion/Features/PipeFeatureInput.h>  // Get the value of the property. FeatureOperations propertyValue = pipeFeatureInput_var->operation();  // Set the value of the property, where value_var is a FeatureOperations. bool returnValue = pipeFeatureInput_var->operation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [FeatureOperations](FeatureOperations.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |