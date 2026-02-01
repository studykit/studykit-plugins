# TrimFeatureInput.objectType Property

Parent Object: [TrimFeatureInput](TrimFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TrimFeatureInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"trimFeatureInput\_var" is a variable referencing a TrimFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = trimFeatureInput_var.objectType ``` ```` |

"trimFeatureInput\_var" is a variable referencing a TrimFeatureInput object. ```` ``` #include <Fusion/Features/TrimFeatureInput.h>  // Get the value of the property. string propertyValue = trimFeatureInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |