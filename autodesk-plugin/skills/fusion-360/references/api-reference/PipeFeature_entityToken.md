# PipeFeature.entityToken Property

Parent Object: [PipeFeature](PipeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeature.h>

## Description

Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeature\_var" is a variable referencing a PipeFeature object.  ```` ``` # Get the value of the property. propertyValue = pipeFeature_var.entityToken ``` ```` |

"pipeFeature\_var" is a variable referencing a PipeFeature object. ```` ``` #include <Fusion/Features/PipeFeature.h>  // Get the value of the property. string propertyValue = pipeFeature_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |