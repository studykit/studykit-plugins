# CollinearConstraint.isValid Property

Parent Object: [CollinearConstraint](CollinearConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CollinearConstraint.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"collinearConstraint\_var" is a variable referencing a CollinearConstraint object. |

"collinearConstraint\_var" is a variable referencing a CollinearConstraint object. ```` ``` #include <Fusion/Sketch/CollinearConstraint.h>  // Get the value of the property. boolean propertyValue = collinearConstraint_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |