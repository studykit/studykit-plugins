# SilhouetteSplitFeatures.add Method

Parent Object: [SilhouetteSplitFeatures](SilhouetteSplitFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SilhouetteSplitFeatures.h>

## Description

Creates a new silhouette split feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"silhouetteSplitFeatures\_var" is a variable referencing a [SilhouetteSplitFeatures](SilhouetteSplitFeatures.htm) object.```` ``` returnValue = silhouetteSplitFeatures_var.add(input) ``` ```` |

"silhouetteSplitFeatures\_var" is a variable referencing a [SilhouetteSplitFeatures](SilhouetteSplitFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SilhouetteSplitFeature](SilhouetteSplitFeature.htm) | Returns the newly created SilhouetteSplitFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [SilhouetteSplitFeatureInput](SilhouetteSplitFeatureInput.htm) | A SilhouetteSplitFeatureInput object that defines the desired silhouette split feature. Use the createInput method to create a new SilhouetteSplitFeatureInput object and then use methods on it (the SilhouetteSplitFeatureInput object) to define the silhouette split. |

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