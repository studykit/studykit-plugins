# PipeFeatureInput.creationOccurrence Property

Parent Object: [PipeFeatureInput](PipeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeatureInput.h>

## Description

In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the Pipe is created based on geometry (e.g. a path) in another component AND (the Pipe) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeatureInput\_var" is a variable referencing a PipeFeatureInput object. |

"pipeFeatureInput\_var" is a variable referencing a PipeFeatureInput object. ```` ``` #include <Fusion/Features/PipeFeatureInput.h>  // Get the value of the property. Ptr<Occurrence> propertyValue = pipeFeatureInput_var->creationOccurrence();  // Set the value of the property, where value_var is an Occurrence. bool returnValue = pipeFeatureInput_var->creationOccurrence(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [Occurrence](Occurrence.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |