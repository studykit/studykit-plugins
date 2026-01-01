# SilhouetteSplitFeatures.itemByName Method

Parent Object: [SilhouetteSplitFeatures](SilhouetteSplitFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SilhouetteSplitFeatures.h>

## Description

Function that returns the specified silhouette split feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"silhouetteSplitFeatures\_var" is a variable referencing a [SilhouetteSplitFeatures](SilhouetteSplitFeatures.htm) object.```` ``` returnValue = silhouetteSplitFeatures_var.itemByName(name) ``` ```` |

"silhouetteSplitFeatures\_var" is a variable referencing a [SilhouetteSplitFeatures](SilhouetteSplitFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SilhouetteSplitFeature](SilhouetteSplitFeature.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the feature within the collection to return. This is the name seen in the timeline. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |