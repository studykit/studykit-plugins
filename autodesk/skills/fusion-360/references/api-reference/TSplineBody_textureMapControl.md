# TSplineBody.textureMapControl Property

Parent Object: [TSplineBody](TSplineBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/TSpline/TSplineBody.h>

## Description

Returns the TextureMapControl object associated with this body when there is an appearance assigned to the body that has a texture associated with it. If there isn't a texture, this property will return null. If there is a texture, you can use the returned object to query and modify how the texture is applied to the body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tSplineBody\_var" is a variable referencing a TSplineBody object. |

"tSplineBody\_var" is a variable referencing a TSplineBody object. ```` ``` #include <Fusion/TSpline/TSplineBody.h>  // Get the value of the property. Ptr<TextureMapControl> propertyValue = tSplineBody_var->textureMapControl(); ``` ```` |

## Property Value

This is a read only property whose value is a [TextureMapControl](TextureMapControl.htm).

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |