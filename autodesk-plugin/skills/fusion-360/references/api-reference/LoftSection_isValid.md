# LoftSection.isValid Property

Parent Object: [LoftSection](LoftSection.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftSection.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftSection\_var" is a variable referencing a LoftSection object. |

"loftSection\_var" is a variable referencing a LoftSection object. ```` ``` #include <Fusion/Features/LoftSection.h>  // Get the value of the property. boolean propertyValue = loftSection_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |