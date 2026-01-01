# UnfoldFeatures.objectType Property

Parent Object: [UnfoldFeatures](UnfoldFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/UnfoldFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unfoldFeatures\_var" is a variable referencing a UnfoldFeatures object.  ```` ``` # Get the value of the property. propertyValue = unfoldFeatures_var.objectType ``` ```` |

"unfoldFeatures\_var" is a variable referencing a UnfoldFeatures object. ```` ``` #include <Fusion/SheetMetal/UnfoldFeatures.h>  // Get the value of the property. string propertyValue = unfoldFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |