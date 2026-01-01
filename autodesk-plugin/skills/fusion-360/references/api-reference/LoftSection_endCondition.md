# LoftSection.endCondition Property

Parent Object: [LoftSection](LoftSection.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftSection.h>

## Description

Returns the current end condition. This is only valid for the first and last section and when the result is not closed. In other cases this will return null. This returns one of the several objects derived from LoftEndCondition and represents the current end condition. You can edit the existing condition using properties on the returned object. You can change the end condition using one of the set methods on the LoftSection object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftSection\_var" is a variable referencing a LoftSection object.  ```` ``` # Get the value of the property. propertyValue = loftSection_var.endCondition ``` ```` |

"loftSection\_var" is a variable referencing a LoftSection object. ```` ``` #include <Fusion/Features/LoftSection.h>  // Get the value of the property. Ptr<LoftEndCondition> propertyValue = loftSection_var->endCondition(); ``` ```` |

## Property Value

This is a read only property whose value is a [LoftEndCondition](LoftEndCondition.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |