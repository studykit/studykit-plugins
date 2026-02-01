# ThickenFeature.isValid Property

Parent Object: [ThickenFeature](ThickenFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThickenFeature.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"thickenFeature\_var" is a variable referencing a ThickenFeature object. |

"thickenFeature\_var" is a variable referencing a ThickenFeature object. ```` ``` #include <Fusion/Features/ThickenFeature.h>  // Get the value of the property. boolean propertyValue = thickenFeature_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |