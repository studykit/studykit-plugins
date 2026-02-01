# PipeFeatures.isValid Property

Parent Object: [PipeFeatures](PipeFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeatures\_var" is a variable referencing a PipeFeatures object. |

"pipeFeatures\_var" is a variable referencing a PipeFeatures object. ```` ``` #include <Fusion/Features/PipeFeatures.h>  // Get the value of the property. boolean propertyValue = pipeFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |