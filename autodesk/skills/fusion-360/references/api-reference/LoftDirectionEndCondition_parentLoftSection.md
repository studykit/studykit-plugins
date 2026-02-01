# LoftDirectionEndCondition.parentLoftSection Property

Parent Object: [LoftDirectionEndCondition](LoftDirectionEndCondition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftDirectionEndCondition.h>

## Description

Returns the parent loft section.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftDirectionEndCondition\_var" is a variable referencing a LoftDirectionEndCondition object. |

"loftDirectionEndCondition\_var" is a variable referencing a LoftDirectionEndCondition object. ```` ``` #include <Fusion/Features/LoftDirectionEndCondition.h>  // Get the value of the property. Ptr<LoftSection> propertyValue = loftDirectionEndCondition_var->parentLoftSection(); ``` ```` |

## Property Value

This is a read only property whose value is a [LoftSection](LoftSection.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |