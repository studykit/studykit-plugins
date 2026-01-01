# LoftPointTangentEndCondition.parentLoftSection Property

Parent Object: [LoftPointTangentEndCondition](LoftPointTangentEndCondition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftPointTangentEndCondition.h>

## Description

Returns the parent loft section.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftPointTangentEndCondition\_var" is a variable referencing a LoftPointTangentEndCondition object. |

"loftPointTangentEndCondition\_var" is a variable referencing a LoftPointTangentEndCondition object. ```` ``` #include <Fusion/Features/LoftPointTangentEndCondition.h>  // Get the value of the property. Ptr<LoftSection> propertyValue = loftPointTangentEndCondition_var->parentLoftSection(); ``` ```` |

## Property Value

This is a read only property whose value is a [LoftSection](LoftSection.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |