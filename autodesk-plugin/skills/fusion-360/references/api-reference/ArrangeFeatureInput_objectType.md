# ArrangeFeatureInput.objectType Property

Parent Object: [ArrangeFeatureInput](ArrangeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeFeatureInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeFeatureInput\_var" is a variable referencing an ArrangeFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = arrangeFeatureInput_var.objectType ``` ```` |

"arrangeFeatureInput\_var" is a variable referencing an ArrangeFeatureInput object. ```` ``` #include <Fusion/Arrange/ArrangeFeatureInput.h>  // Get the value of the property. string propertyValue = arrangeFeatureInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |