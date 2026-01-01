# ExtendFeatureInput.extendAlignment Property

Parent Object: [ExtendFeatureInput](ExtendFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtendFeatureInput.h>

## Description

Gets and sets surface extend alignment to use.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extendFeatureInput\_var" is a variable referencing an ExtendFeatureInput object. |

"extendFeatureInput\_var" is a variable referencing an ExtendFeatureInput object. ```` ``` #include <Fusion/Features/ExtendFeatureInput.h>  // Get the value of the property. SurfaceExtendAlignment propertyValue = extendFeatureInput_var->extendAlignment();  // Set the value of the property, where value_var is a SurfaceExtendAlignment. bool returnValue = extendFeatureInput_var->extendAlignment(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SurfaceExtendAlignment](SurfaceExtendAlignment.htm).

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |