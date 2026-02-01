# ProjectedTextureMapControl.objectType Property

Parent Object: [ProjectedTextureMapControl](ProjectedTextureMapControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/ProjectedTextureMapControl.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"projectedTextureMapControl\_var" is a variable referencing a ProjectedTextureMapControl object.  ```` ``` # Get the value of the property. propertyValue = projectedTextureMapControl_var.objectType ``` ```` |

"projectedTextureMapControl\_var" is a variable referencing a ProjectedTextureMapControl object. ```` ``` #include <Core/Materials/ProjectedTextureMapControl.h>  // Get the value of the property. string propertyValue = projectedTextureMapControl_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |