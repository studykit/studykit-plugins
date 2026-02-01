# FilletFeatureInput.objectType Property

Parent Object: [FilletFeatureInput](FilletFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletFeatureInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletFeatureInput\_var" is a variable referencing a FilletFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = filletFeatureInput_var.objectType ``` ```` |

"filletFeatureInput\_var" is a variable referencing a FilletFeatureInput object. ```` ``` #include <Fusion/Features/FilletFeatureInput.h>  // Get the value of the property. string propertyValue = filletFeatureInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |