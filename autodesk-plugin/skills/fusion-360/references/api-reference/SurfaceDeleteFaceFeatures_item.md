# SurfaceDeleteFaceFeatures.item Method

Parent Object: [SurfaceDeleteFaceFeatures](SurfaceDeleteFaceFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SurfaceDeleteFaceFeatures.h>

## Description

Function that returns the specified SurfaceDeleteFaceFeature object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceDeleteFaceFeatures\_var" is a variable referencing a [SurfaceDeleteFaceFeatures](SurfaceDeleteFaceFeatures.htm) object.```` ``` returnValue = surfaceDeleteFaceFeatures_var.item(index) ``` ```` |

"surfaceDeleteFaceFeatures\_var" is a variable referencing a [SurfaceDeleteFaceFeatures](SurfaceDeleteFaceFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SurfaceDeleteFaceFeature](SurfaceDeleteFaceFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |