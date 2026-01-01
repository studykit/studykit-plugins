# LoftSection.setFreeEndCondition Method

Parent Object: [LoftSection](LoftSection.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftSection.h>

## Description

Sets the end condition to be a "Free" end condition. This is the default end condition when a new section is added.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftSection\_var" is a variable referencing a [LoftSection](LoftSection.htm) object.```` ``` returnValue = loftSection_var.setFreeEndCondition() ``` ```` |

"loftSection\_var" is a variable referencing a [LoftSection](LoftSection.htm) object.  ```` ``` #include <Fusion/Features/LoftSection.h>  returnValue = loftSection_var->setFreeEndCondition(); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the operation was successful. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |