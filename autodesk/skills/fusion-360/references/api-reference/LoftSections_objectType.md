# LoftSections.objectType Property

Parent Object: [LoftSections](LoftSections.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftSections.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftSections\_var" is a variable referencing a LoftSections object.  ```` ``` # Get the value of the property. propertyValue = loftSections_var.objectType ``` ```` |

"loftSections\_var" is a variable referencing a LoftSections object. ```` ``` #include <Fusion/Features/LoftSections.h>  // Get the value of the property. string propertyValue = loftSections_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |