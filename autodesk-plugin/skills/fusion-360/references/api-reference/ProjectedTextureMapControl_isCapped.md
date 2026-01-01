# ProjectedTextureMapControl.isCapped Property

Parent Object: [ProjectedTextureMapControl](ProjectedTextureMapControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/ProjectedTextureMapControl.h>

## Description

When a cylindrical projected texture map is being used this property gets and sets if a cap is use for the cylindrical projection. This property is only valid in the case when the projectedTextureMapType returns CylindricalTextureMapProjection. The value of this property should be ignored in all other cases and setting the property will have no effect.

## Syntax

* [Python](#Python)
* [C++](#C++)

"projectedTextureMapControl\_var" is a variable referencing a ProjectedTextureMapControl object. |

"projectedTextureMapControl\_var" is a variable referencing a ProjectedTextureMapControl object. ```` ``` #include <Core/Materials/ProjectedTextureMapControl.h>  // Get the value of the property. boolean propertyValue = projectedTextureMapControl_var->isCapped();  // Set the value of the property, where value_var is a boolean. bool returnValue = projectedTextureMapControl_var->isCapped(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |