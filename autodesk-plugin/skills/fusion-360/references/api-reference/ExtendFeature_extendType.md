# ExtendFeature.extendType Property

Parent Object: [ExtendFeature](ExtendFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtendFeature.h>

## Description

Gets and sets surface extend type to use.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extendFeature\_var" is a variable referencing an ExtendFeature object.  ```` ``` # Get the value of the property. propertyValue = extendFeature_var.extendType  # Set the value of the property. extendFeature_var.extendType = propertyValue ``` ```` |

"extendFeature\_var" is a variable referencing an ExtendFeature object. ```` ``` #include <Fusion/Features/ExtendFeature.h>  // Get the value of the property. SurfaceExtendTypes propertyValue = extendFeature_var->extendType();  // Set the value of the property, where value_var is a SurfaceExtendTypes. bool returnValue = extendFeature_var->extendType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SurfaceExtendTypes](SurfaceExtendTypes.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |