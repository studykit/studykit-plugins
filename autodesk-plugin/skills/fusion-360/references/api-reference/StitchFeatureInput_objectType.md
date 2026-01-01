# StitchFeatureInput.objectType Property

Parent Object: [StitchFeatureInput](StitchFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/StitchFeatureInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stitchFeatureInput\_var" is a variable referencing a StitchFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = stitchFeatureInput_var.objectType ``` ```` |

"stitchFeatureInput\_var" is a variable referencing a StitchFeatureInput object. ```` ``` #include <Fusion/Features/StitchFeatureInput.h>  // Get the value of the property. string propertyValue = stitchFeatureInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |