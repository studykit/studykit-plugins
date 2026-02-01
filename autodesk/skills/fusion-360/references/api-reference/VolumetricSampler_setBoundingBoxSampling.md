# VolumetricSampler.setBoundingBoxSampling Method![](../images/TestTubeLarge.png)

Parent Object: [VolumetricSampler](VolumetricSampler.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::volume" and the header file is <Volume/Volumetric/VolumetricSampler.h>

## Description

Calculates and sets the sample points to be used for sampling the volumetric model for a given resolution throughout the bounding box provided. This will override any previously set sample points.

## Syntax

* [Python](#Python)
* [C++](#C++)

"volumetricSampler\_var" is a variable referencing a [VolumetricSampler](VolumetricSampler.htm) object.```` ``` returnValue = volumetricSampler_var.setBoundingBoxSampling(elementSize, boundingBox3d) ``` ```` |

"volumetricSampler\_var" is a variable referencing a [VolumetricSampler](VolumetricSampler.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | True if the sample points were set successfully. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| elementSize | double | The approximate spacing between sample points. The units used for the element size are centimeters. |
| boundingBox3d | [BoundingBox3D](BoundingBox3D.htm) | The bounding box in which the sample points will be distributed. |

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |