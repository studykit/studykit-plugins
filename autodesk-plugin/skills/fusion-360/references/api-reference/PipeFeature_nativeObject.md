# PipeFeature.nativeObject Property

Parent Object: [PipeFeature](PipeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeature.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeature\_var" is a variable referencing a PipeFeature object. |

"pipeFeature\_var" is a variable referencing a PipeFeature object. ```` ``` #include <Fusion/Features/PipeFeature.h>  // Get the value of the property. Ptr<PipeFeature> propertyValue = pipeFeature_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [PipeFeature](PipeFeature.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |