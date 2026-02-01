# MeshBodyList.objectType Property

Parent Object: [MeshBodyList](MeshBodyList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBodyList.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshBodyList\_var" is a variable referencing a MeshBodyList object.  ```` ``` # Get the value of the property. propertyValue = meshBodyList_var.objectType ``` ```` |

"meshBodyList\_var" is a variable referencing a MeshBodyList object. ```` ``` #include <Fusion/MeshBody/MeshBodyList.h>  // Get the value of the property. string propertyValue = meshBodyList_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |