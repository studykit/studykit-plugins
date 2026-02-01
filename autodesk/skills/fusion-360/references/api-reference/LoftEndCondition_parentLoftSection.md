# LoftEndCondition.parentLoftSection Property

Parent Object: [LoftEndCondition](LoftEndCondition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftEndCondition.h>

## Description

Returns the parent loft section.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftEndCondition\_var" is a variable referencing a LoftEndCondition object. |

"loftEndCondition\_var" is a variable referencing a LoftEndCondition object. ```` ``` #include <Fusion/Features/LoftEndCondition.h>  // Get the value of the property. Ptr<LoftSection> propertyValue = loftEndCondition_var->parentLoftSection(); ``` ```` |

## Property Value

This is a read only property whose value is a [LoftSection](LoftSection.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |