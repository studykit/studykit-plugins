# UntrimFeatureInput.objectType Property

Parent Object: [UntrimFeatureInput](UntrimFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UntrimFeatureInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"untrimFeatureInput\_var" is a variable referencing a UntrimFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = untrimFeatureInput_var.objectType ``` ```` |

"untrimFeatureInput\_var" is a variable referencing a UntrimFeatureInput object. ```` ``` #include <Fusion/Features/UntrimFeatureInput.h>  // Get the value of the property. string propertyValue = untrimFeatureInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |