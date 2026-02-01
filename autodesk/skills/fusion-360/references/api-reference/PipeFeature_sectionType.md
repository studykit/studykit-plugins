# PipeFeature.sectionType Property

Parent Object: [PipeFeature](PipeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeature.h>

## Description

Gets and sets the section type of the Pipe. The type can be: Circular, Square, Triangular.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeature\_var" is a variable referencing a PipeFeature object. |

"pipeFeature\_var" is a variable referencing a PipeFeature object. ```` ``` #include <Fusion/Features/PipeFeature.h>  // Get the value of the property. PipeSectionTypes propertyValue = pipeFeature_var->sectionType();  // Set the value of the property, where value_var is a PipeSectionTypes. bool returnValue = pipeFeature_var->sectionType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PipeSectionTypes](PipeSectionTypes.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |