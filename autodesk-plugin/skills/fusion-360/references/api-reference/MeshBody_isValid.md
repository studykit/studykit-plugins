# MeshBody.isValid Property

Parent Object: [MeshBody](MeshBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBody.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshBody\_var" is a variable referencing a MeshBody object. |

"meshBody\_var" is a variable referencing a MeshBody object. ```` ``` #include <Fusion/MeshBody/MeshBody.h>  // Get the value of the property. boolean propertyValue = meshBody_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |