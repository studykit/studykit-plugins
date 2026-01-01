# LoftFeatureInput.centerLineOrRails Property

Parent Object: [LoftFeatureInput](LoftFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFeatureInput.h>

## Description

The single centerline or set of rails that define the shape of the loft. Use methods on the returned LoftCenterLineOrRails object to define the centerline or rails.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFeatureInput\_var" is a variable referencing a LoftFeatureInput object. |

"loftFeatureInput\_var" is a variable referencing a LoftFeatureInput object. ```` ``` #include <Fusion/Features/LoftFeatureInput.h>  // Get the value of the property. Ptr<LoftCenterLineOrRails> propertyValue = loftFeatureInput_var->centerLineOrRails(); ``` ```` |

## Property Value

This is a read only property whose value is a [LoftCenterLineOrRails](LoftCenterLineOrRails.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |