# ScaleFeatureInput.objectType Property

Parent Object: [ScaleFeatureInput](ScaleFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ScaleFeatureInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scaleFeatureInput\_var" is a variable referencing a ScaleFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = scaleFeatureInput_var.objectType ``` ```` |

"scaleFeatureInput\_var" is a variable referencing a ScaleFeatureInput object. ```` ``` #include <Fusion/Features/ScaleFeatureInput.h>  // Get the value of the property. string propertyValue = scaleFeatureInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |