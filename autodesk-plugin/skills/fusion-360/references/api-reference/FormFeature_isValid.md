# FormFeature.isValid Property

Parent Object: [FormFeature](FormFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FormFeature.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"formFeature\_var" is a variable referencing a FormFeature object. |

"formFeature\_var" is a variable referencing a FormFeature object. ```` ``` #include <Fusion/Features/FormFeature.h>  // Get the value of the property. boolean propertyValue = formFeature_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |