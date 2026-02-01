# MeshBodyDisplayOverrides.isSuppressFaceGroupColors Property

Parent Object: [MeshBodyDisplayOverrides](MeshBodyDisplayOverrides.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBodyDisplayOverrides.h>

## Description

Controls whether the mesh body face group colors are shown. If set to true, the face groups will be shown with the assigned appearance, ignoring the current display settings.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshBodyDisplayOverrides\_var" is a variable referencing a MeshBodyDisplayOverrides object. |

"meshBodyDisplayOverrides\_var" is a variable referencing a MeshBodyDisplayOverrides object. ```` ``` #include <Fusion/MeshBody/MeshBodyDisplayOverrides.h>  // Get the value of the property. boolean propertyValue = meshBodyDisplayOverrides_var->isSuppressFaceGroupColors();  // Set the value of the property, where value_var is a boolean. bool returnValue = meshBodyDisplayOverrides_var->isSuppressFaceGroupColors(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |