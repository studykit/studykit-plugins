# LoftSections.isValid Property

Parent Object: [LoftSections](LoftSections.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftSections.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftSections\_var" is a variable referencing a LoftSections object. |

"loftSections\_var" is a variable referencing a LoftSections object. ```` ``` #include <Fusion/Features/LoftSections.h>  // Get the value of the property. boolean propertyValue = loftSections_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |