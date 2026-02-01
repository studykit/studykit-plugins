# PipeFeature.isHollow Property

Parent Object: [PipeFeature](PipeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeature.h>

## Description

Specifies if the Pipe is hollow or not.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeature\_var" is a variable referencing a PipeFeature object.  ```` ``` # Get the value of the property. propertyValue = pipeFeature_var.isHollow  # Set the value of the property. pipeFeature_var.isHollow = propertyValue ``` ```` |

"pipeFeature\_var" is a variable referencing a PipeFeature object. ```` ``` #include <Fusion/Features/PipeFeature.h>  // Get the value of the property. boolean propertyValue = pipeFeature_var->isHollow();  // Set the value of the property, where value_var is a boolean. bool returnValue = pipeFeature_var->isHollow(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |