# Features.silhouetteSplitFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the Parting Line Split features within the component and supports the creation of new Parting Line Split features

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<SilhouetteSplitFeatures> propertyValue = features_var->silhouetteSplitFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [SilhouetteSplitFeatures](SilhouetteSplitFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [silhouetteSplitFeatures.add](silhouetteSplitFeatures_add_Sample.htm) | Demonstrates the silhouetteSplitFeatures.add method. The Silhouette Split feature is limited in the bodies it will split. The simplest body to get a valid result is to create a sphere and split it. |
| [Silhouette Split Feature API Sample](SilhouetteSplitFeatureSample_Sample.htm) | Demonstrates creating a new silhouette split feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |