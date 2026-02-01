# Features.boundaryFillFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the Boundary Fill features within the component and supports the creation of new Boundary Fill features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<BoundaryFillFeatures> propertyValue = features_var->boundaryFillFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [BoundaryFillFeatures](BoundaryFillFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [boundaryFillFeatures.add](boundaryFillFeatures_add_Sample.htm) | Demonstrates the boundaryFill.add method. To use this sample you need to have two existing overlapping bodies. You'll be prompted to select the bodies when running the script. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |