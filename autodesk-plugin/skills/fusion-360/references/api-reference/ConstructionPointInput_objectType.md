# ConstructionPointInput.objectType Property

Parent Object: [ConstructionPointInput](ConstructionPointInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPointInput\_var" is a variable referencing a ConstructionPointInput object.  ```` ``` # Get the value of the property. propertyValue = constructionPointInput_var.objectType ``` ```` |

"constructionPointInput\_var" is a variable referencing a ConstructionPointInput object. ```` ``` #include <Fusion/Construction/ConstructionPointInput.h>  // Get the value of the property. string propertyValue = constructionPointInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |