# TextureMapControl.isValid Property

Parent Object: [TextureMapControl](TextureMapControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/TextureMapControl.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"textureMapControl\_var" is a variable referencing a TextureMapControl object. |

"textureMapControl\_var" is a variable referencing a TextureMapControl object. ```` ``` #include <Core/Materials/TextureMapControl.h>  // Get the value of the property. boolean propertyValue = textureMapControl_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |