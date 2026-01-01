# ProjectedTextureMapControl.projectedTextureMapType Property

Parent Object: [ProjectedTextureMapControl](ProjectedTextureMapControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/ProjectedTextureMapControl.h>

## Description

Gets and sets how the texture map is being applied onto the body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"projectedTextureMapControl\_var" is a variable referencing a ProjectedTextureMapControl object. |

"projectedTextureMapControl\_var" is a variable referencing a ProjectedTextureMapControl object. ```` ``` #include <Core/Materials/ProjectedTextureMapControl.h>  // Get the value of the property. ProjectedTextureMapTypes propertyValue = projectedTextureMapControl_var->projectedTextureMapType();  // Set the value of the property, where value_var is a ProjectedTextureMapTypes. bool returnValue = projectedTextureMapControl_var->projectedTextureMapType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ProjectedTextureMapTypes](ProjectedTextureMapTypes.htm).

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |