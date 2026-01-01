# ProfilePlaneStartDefinition.objectType Property

Parent Object: [ProfilePlaneStartDefinition](ProfilePlaneStartDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ProfilePlaneStartDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profilePlaneStartDefinition\_var" is a variable referencing a ProfilePlaneStartDefinition object.  ```` ``` # Get the value of the property. propertyValue = profilePlaneStartDefinition_var.objectType ``` ```` |

"profilePlaneStartDefinition\_var" is a variable referencing a ProfilePlaneStartDefinition object. ```` ``` #include <Fusion/Features/ProfilePlaneStartDefinition.h>  // Get the value of the property. string propertyValue = profilePlaneStartDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |