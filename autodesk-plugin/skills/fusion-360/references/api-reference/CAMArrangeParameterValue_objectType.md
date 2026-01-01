# CAMArrangeParameterValue.objectType Property

Parent Object: [CAMArrangeParameterValue](CAMArrangeParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CAMArrangeParameterValue.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMArrangeParameterValue\_var" is a variable referencing a CAMArrangeParameterValue object.  ```` ``` # Get the value of the property. propertyValue = cAMArrangeParameterValue_var.objectType ``` ```` |

"cAMArrangeParameterValue\_var" is a variable referencing a CAMArrangeParameterValue object. ```` ``` #include <Cam/Operations/CAMArrangeParameterValue.h>  // Get the value of the property. string propertyValue = cAMArrangeParameterValue_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |