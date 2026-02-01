# FormFeatures.isValid Property

Parent Object: [FormFeatures](FormFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FormFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"formFeatures\_var" is a variable referencing a FormFeatures object. |

"formFeatures\_var" is a variable referencing a FormFeatures object. ```` ``` #include <Fusion/Features/FormFeatures.h>  // Get the value of the property. boolean propertyValue = formFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |