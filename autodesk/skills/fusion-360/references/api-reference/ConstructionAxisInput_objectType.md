# ConstructionAxisInput.objectType Property

Parent Object: [ConstructionAxisInput](ConstructionAxisInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxisInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxisInput\_var" is a variable referencing a ConstructionAxisInput object.  ```` ``` # Get the value of the property. propertyValue = constructionAxisInput_var.objectType ``` ```` |

"constructionAxisInput\_var" is a variable referencing a ConstructionAxisInput object. ```` ``` #include <Fusion/Construction/ConstructionAxisInput.h>  // Get the value of the property. string propertyValue = constructionAxisInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |