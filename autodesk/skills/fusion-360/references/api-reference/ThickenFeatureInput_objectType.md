# ThickenFeatureInput.objectType Property

Parent Object: [ThickenFeatureInput](ThickenFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThickenFeatureInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"thickenFeatureInput\_var" is a variable referencing a ThickenFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = thickenFeatureInput_var.objectType ``` ```` |

"thickenFeatureInput\_var" is a variable referencing a ThickenFeatureInput object. ```` ``` #include <Fusion/Features/ThickenFeatureInput.h>  // Get the value of the property. string propertyValue = thickenFeatureInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |