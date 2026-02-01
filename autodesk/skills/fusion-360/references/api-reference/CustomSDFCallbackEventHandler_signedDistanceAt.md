# CustomSDFCallbackEventHandler.signedDistanceAt Method![](../images/TestTubeLarge.png)

Parent Object: [CustomSDFCallbackEventHandler](CustomSDFCallbackEventHandler.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::volume" and the header file is <Volume/Volumetric/CustomSDFCallbackEventHandler.h>

## Description

This method should be implemented in the subclass of the handler to return the Signed Distance value at the given coordinates within the bounding box. This method will be called very frequently and potentially from several differrent threads, it should be made as fast as possible

## Syntax

* [Python](#Python)
* [C++](#C++)

"customSDFCallbackEventHandler\_var" is a variable referencing a [CustomSDFCallbackEventHandler](CustomSDFCallbackEventHandler.htm) object.```` ``` returnValue = customSDFCallbackEventHandler_var.signedDistanceAt(x, y, z) ``` ```` |

"customSDFCallbackEventHandler\_var" is a variable referencing a [CustomSDFCallbackEventHandler](CustomSDFCallbackEventHandler.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| double | The signed distance value at the sampled point (X,Y,Z). |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| x | double | X coordinate of the sampled point. |
| y | double | Y coordinate of the sampled point. |
| z | double | Z coordinate of the sampled point. |

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |