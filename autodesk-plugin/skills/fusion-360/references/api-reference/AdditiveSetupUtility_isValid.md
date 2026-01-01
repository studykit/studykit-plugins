# AdditiveSetupUtility.isValid Property

Parent Object: [AdditiveSetupUtility](AdditiveSetupUtility.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/ModifyUtility/AdditiveSetupUtility.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"additiveSetupUtility\_var" is a variable referencing an AdditiveSetupUtility object. |

"additiveSetupUtility\_var" is a variable referencing an AdditiveSetupUtility object. ```` ``` #include <Cam/ModifyUtility/AdditiveSetupUtility.h>  // Get the value of the property. boolean propertyValue = additiveSetupUtility_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |