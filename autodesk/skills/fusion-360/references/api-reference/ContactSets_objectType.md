# ContactSets.objectType Property

Parent Object: [ContactSets](ContactSets.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/ContactSets.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"contactSets\_var" is a variable referencing a ContactSets object.  ```` ``` # Get the value of the property. propertyValue = contactSets_var.objectType ``` ```` |

"contactSets\_var" is a variable referencing a ContactSets object. ```` ``` #include <Fusion/Components/ContactSets.h>  // Get the value of the property. string propertyValue = contactSets_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |