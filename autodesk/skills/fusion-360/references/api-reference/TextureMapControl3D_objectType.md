# TextureMapControl3D.objectType Property

Parent Object: [TextureMapControl3D](TextureMapControl3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/TextureMapControl3D.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"textureMapControl3D\_var" is a variable referencing a TextureMapControl3D object.  ```` ``` # Get the value of the property. propertyValue = textureMapControl3D_var.objectType ``` ```` |

"textureMapControl3D\_var" is a variable referencing a TextureMapControl3D object. ```` ``` #include <Core/Materials/TextureMapControl3D.h>  // Get the value of the property. string propertyValue = textureMapControl3D_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |