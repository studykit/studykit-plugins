# PipeFeatureInput.sectionThickness Property

Parent Object: [PipeFeatureInput](PipeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeatureInput.h>

## Description

Gets and sets the section thickness of the Pipe.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeatureInput\_var" is a variable referencing a PipeFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = pipeFeatureInput_var.sectionThickness  # Set the value of the property. pipeFeatureInput_var.sectionThickness = propertyValue ``` ```` |

"pipeFeatureInput\_var" is a variable referencing a PipeFeatureInput object. ```` ``` #include <Fusion/Features/PipeFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = pipeFeatureInput_var->sectionThickness();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = pipeFeatureInput_var->sectionThickness(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |