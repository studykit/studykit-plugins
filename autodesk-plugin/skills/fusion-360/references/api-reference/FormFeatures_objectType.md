# FormFeatures.objectType Property

Parent Object: [FormFeatures](FormFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FormFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"formFeatures\_var" is a variable referencing a FormFeatures object.  ```` ``` # Get the value of the property. propertyValue = formFeatures_var.objectType ``` ```` |

"formFeatures\_var" is a variable referencing a FormFeatures object. ```` ``` #include <Fusion/Features/FormFeatures.h>  // Get the value of the property. string propertyValue = formFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |