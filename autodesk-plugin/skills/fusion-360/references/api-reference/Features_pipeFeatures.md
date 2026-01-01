# Features.pipeFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the existing pipe features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<PipeFeatures> propertyValue = features_var->pipeFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [PipeFeatures](PipeFeatures.htm).

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |