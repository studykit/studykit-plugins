# ContactSet.objectType Property

Parent Object: [ContactSet](ContactSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/ContactSet.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"contactSet\_var" is a variable referencing a ContactSet object.  ```` ``` # Get the value of the property. propertyValue = contactSet_var.objectType ``` ```` |

"contactSet\_var" is a variable referencing a ContactSet object. ```` ``` #include <Fusion/Components/ContactSet.h>  // Get the value of the property. string propertyValue = contactSet_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |