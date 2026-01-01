# LoftFreeEndCondition.parentLoftSection Property

Parent Object: [LoftFreeEndCondition](LoftFreeEndCondition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFreeEndCondition.h>

## Description

Returns the parent loft section.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFreeEndCondition\_var" is a variable referencing a LoftFreeEndCondition object. |

"loftFreeEndCondition\_var" is a variable referencing a LoftFreeEndCondition object. ```` ``` #include <Fusion/Features/LoftFreeEndCondition.h>  // Get the value of the property. Ptr<LoftSection> propertyValue = loftFreeEndCondition_var->parentLoftSection(); ``` ```` |

## Property Value

This is a read only property whose value is a [LoftSection](LoftSection.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |