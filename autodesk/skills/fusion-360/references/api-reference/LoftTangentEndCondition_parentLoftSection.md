# LoftTangentEndCondition.parentLoftSection Property

Parent Object: [LoftTangentEndCondition](LoftTangentEndCondition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftTangentEndCondition.h>

## Description

Returns the parent loft section.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftTangentEndCondition\_var" is a variable referencing a LoftTangentEndCondition object. |

"loftTangentEndCondition\_var" is a variable referencing a LoftTangentEndCondition object. ```` ``` #include <Fusion/Features/LoftTangentEndCondition.h>  // Get the value of the property. Ptr<LoftSection> propertyValue = loftTangentEndCondition_var->parentLoftSection(); ``` ```` |

## Property Value

This is a read only property whose value is a [LoftSection](LoftSection.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |