# AdditiveSetupUtility.objectType Property

Parent Object: [AdditiveSetupUtility](AdditiveSetupUtility.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/ModifyUtility/AdditiveSetupUtility.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"additiveSetupUtility\_var" is a variable referencing an AdditiveSetupUtility object.  ```` ``` # Get the value of the property. propertyValue = additiveSetupUtility_var.objectType ``` ```` |

"additiveSetupUtility\_var" is a variable referencing an AdditiveSetupUtility object. ```` ``` #include <Cam/ModifyUtility/AdditiveSetupUtility.h>  // Get the value of the property. string propertyValue = additiveSetupUtility_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |