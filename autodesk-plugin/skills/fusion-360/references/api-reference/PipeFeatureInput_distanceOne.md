# PipeFeatureInput.distanceOne Property

Parent Object: [PipeFeatureInput](PipeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeatureInput.h>

## Description

Gets and sets the distance for the pipe created while following the path given as input, in the same order. This value defaults to 1.0 if not set.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeatureInput\_var" is a variable referencing a PipeFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = pipeFeatureInput_var.distanceOne  # Set the value of the property. pipeFeatureInput_var.distanceOne = propertyValue ``` ```` |

"pipeFeatureInput\_var" is a variable referencing a PipeFeatureInput object. ```` ``` #include <Fusion/Features/PipeFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = pipeFeatureInput_var->distanceOne();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = pipeFeatureInput_var->distanceOne(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |