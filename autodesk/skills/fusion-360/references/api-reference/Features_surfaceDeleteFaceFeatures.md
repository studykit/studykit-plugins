# Features.surfaceDeleteFaceFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the existing Surface Delete Face features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<SurfaceDeleteFaceFeatures> propertyValue = features_var->surfaceDeleteFaceFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [SurfaceDeleteFaceFeatures](SurfaceDeleteFaceFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [surfaceDeleteFeatures.add](surfaceDeleteFeatures_add_Sample.htm) | Demonstrates the surfaceDeleteFeatures.add method. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |