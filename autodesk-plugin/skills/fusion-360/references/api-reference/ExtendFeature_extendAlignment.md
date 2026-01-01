# ExtendFeature.extendAlignment Property

Parent Object: [ExtendFeature](ExtendFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtendFeature.h>

## Description

Gets and sets surface extend alignment to use.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extendFeature\_var" is a variable referencing an ExtendFeature object.  ```` ``` # Get the value of the property. propertyValue = extendFeature_var.extendAlignment  # Set the value of the property. extendFeature_var.extendAlignment = propertyValue ``` ```` |

"extendFeature\_var" is a variable referencing an ExtendFeature object. ```` ``` #include <Fusion/Features/ExtendFeature.h>  // Get the value of the property. SurfaceExtendAlignment propertyValue = extendFeature_var->extendAlignment();  // Set the value of the property, where value_var is a SurfaceExtendAlignment. bool returnValue = extendFeature_var->extendAlignment(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SurfaceExtendAlignment](SurfaceExtendAlignment.htm).

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |