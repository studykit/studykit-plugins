# CAMTemplate.objectType Property

Parent Object: [CAMTemplate](CAMTemplate.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAMTemplate/CAMTemplate.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMTemplate\_var" is a variable referencing a CAMTemplate object.  ```` ``` # Get the value of the property. propertyValue = cAMTemplate_var.objectType ``` ```` |

"cAMTemplate\_var" is a variable referencing a CAMTemplate object. ```` ``` #include <Cam/CAMTemplate/CAMTemplate.h>  // Get the value of the property. string propertyValue = cAMTemplate_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |