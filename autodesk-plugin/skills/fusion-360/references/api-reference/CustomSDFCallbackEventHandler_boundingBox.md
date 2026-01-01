# CustomSDFCallbackEventHandler.boundingBox Method![](../images/TestTubeLarge.png)

Parent Object: [CustomSDFCallbackEventHandler](CustomSDFCallbackEventHandler.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::volume" and the header file is <Volume/Volumetric/CustomSDFCallbackEventHandler.h>

## Description

This method should be implemented in the subclass of the handler to return the bounding box of the Signed Distance Field that it can provide. This method will be called infrequently by the system.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customSDFCallbackEventHandler\_var" is a variable referencing a [CustomSDFCallbackEventHandler](CustomSDFCallbackEventHandler.htm) object.```` ``` returnValue = customSDFCallbackEventHandler_var.boundingBox(bboxOut) ``` ```` |

"customSDFCallbackEventHandler\_var" is a variable referencing a [CustomSDFCallbackEventHandler](CustomSDFCallbackEventHandler.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | True if there is a valid bounding box. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| bboxOut | [BoundingBox3D](BoundingBox3D.htm) | This is a return parameter. The values of this should be set by the client implementation. |

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |