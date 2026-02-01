# CombineFeatureInput.objectType Property

Parent Object: [CombineFeatureInput](CombineFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CombineFeatureInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"combineFeatureInput\_var" is a variable referencing a CombineFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = combineFeatureInput_var.objectType ``` ```` |

"combineFeatureInput\_var" is a variable referencing a CombineFeatureInput object. ```` ``` #include <Fusion/Features/CombineFeatureInput.h>  // Get the value of the property. string propertyValue = combineFeatureInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |