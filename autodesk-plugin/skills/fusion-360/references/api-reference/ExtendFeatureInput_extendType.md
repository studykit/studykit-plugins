# ExtendFeatureInput.extendType Property

Parent Object: [ExtendFeatureInput](ExtendFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtendFeatureInput.h>

## Description

Gets and sets surface extend type to use

## Syntax

* [Python](#Python)
* [C++](#C++)

"extendFeatureInput\_var" is a variable referencing an ExtendFeatureInput object. |

"extendFeatureInput\_var" is a variable referencing an ExtendFeatureInput object. ```` ``` #include <Fusion/Features/ExtendFeatureInput.h>  // Get the value of the property. SurfaceExtendTypes propertyValue = extendFeatureInput_var->extendType();  // Set the value of the property, where value_var is a SurfaceExtendTypes. bool returnValue = extendFeatureInput_var->extendType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SurfaceExtendTypes](SurfaceExtendTypes.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |