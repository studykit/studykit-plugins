# PipeFeature.parentComponent Property

Parent Object: [PipeFeature](PipeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeature.h>

## Description

Returns the parent component that owns this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeature\_var" is a variable referencing a PipeFeature object. |

"pipeFeature\_var" is a variable referencing a PipeFeature object. ```` ``` #include <Fusion/Features/PipeFeature.h>  // Get the value of the property. Ptr<Component> propertyValue = pipeFeature_var->parentComponent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |