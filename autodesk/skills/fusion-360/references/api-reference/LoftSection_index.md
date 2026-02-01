# LoftSection.index Property

Parent Object: [LoftSection](LoftSection.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftSection.h>

## Description

The position of this LoftSection within the collection. The first section has an index of 0. This is also the order of how the section will be used in the loft. The order can be modified by using the reorder method.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftSection\_var" is a variable referencing a LoftSection object. |

"loftSection\_var" is a variable referencing a LoftSection object. ```` ``` #include <Fusion/Features/LoftSection.h>  // Get the value of the property. integer propertyValue = loftSection_var->index(); ``` ```` |

## Property Value

This is a read only property whose value is an integer.

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |