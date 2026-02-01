# MeshBodyDisplayOverrides.objectType Property

Parent Object: [MeshBodyDisplayOverrides](MeshBodyDisplayOverrides.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBodyDisplayOverrides.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshBodyDisplayOverrides\_var" is a variable referencing a MeshBodyDisplayOverrides object.  ```` ``` # Get the value of the property. propertyValue = meshBodyDisplayOverrides_var.objectType ``` ```` |

"meshBodyDisplayOverrides\_var" is a variable referencing a MeshBodyDisplayOverrides object. ```` ``` #include <Fusion/MeshBody/MeshBodyDisplayOverrides.h>  // Get the value of the property. string propertyValue = meshBodyDisplayOverrides_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |