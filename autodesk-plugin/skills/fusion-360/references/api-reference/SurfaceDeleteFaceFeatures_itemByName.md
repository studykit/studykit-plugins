# SurfaceDeleteFaceFeatures.itemByName Method

Parent Object: [SurfaceDeleteFaceFeatures](SurfaceDeleteFaceFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SurfaceDeleteFaceFeatures.h>

## Description

Function that returns the specified SurfaceDeleteFaceFeature object using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceDeleteFaceFeatures\_var" is a variable referencing a [SurfaceDeleteFaceFeatures](SurfaceDeleteFaceFeatures.htm) object.```` ``` returnValue = surfaceDeleteFaceFeatures_var.itemByName(name) ``` ```` |

"surfaceDeleteFaceFeatures\_var" is a variable referencing a [SurfaceDeleteFaceFeatures](SurfaceDeleteFaceFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SurfaceDeleteFaceFeature](SurfaceDeleteFaceFeature.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the feature within the collection to return. This is the name seen in the timeline. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |