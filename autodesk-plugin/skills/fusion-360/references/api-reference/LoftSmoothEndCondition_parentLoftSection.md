# LoftSmoothEndCondition.parentLoftSection Property

Parent Object: [LoftSmoothEndCondition](LoftSmoothEndCondition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftSmoothEndCondition.h>

## Description

Returns the parent loft section.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftSmoothEndCondition\_var" is a variable referencing a LoftSmoothEndCondition object. |

"loftSmoothEndCondition\_var" is a variable referencing a LoftSmoothEndCondition object. ```` ``` #include <Fusion/Features/LoftSmoothEndCondition.h>  // Get the value of the property. Ptr<LoftSection> propertyValue = loftSmoothEndCondition_var->parentLoftSection(); ``` ```` |

## Property Value

This is a read only property whose value is a [LoftSection](LoftSection.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |