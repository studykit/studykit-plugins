# PipeFeatureInput.sectionType Property

Parent Object: [PipeFeatureInput](PipeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeatureInput.h>

## Description

Gets and sets the section type of the Pipe. The type can be: Circular, Square, Triangular.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeatureInput\_var" is a variable referencing a PipeFeatureInput object. |

"pipeFeatureInput\_var" is a variable referencing a PipeFeatureInput object. ```` ``` #include <Fusion/Features/PipeFeatureInput.h>  // Get the value of the property. PipeSectionTypes propertyValue = pipeFeatureInput_var->sectionType();  // Set the value of the property, where value_var is a PipeSectionTypes. bool returnValue = pipeFeatureInput_var->sectionType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PipeSectionTypes](PipeSectionTypes.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |