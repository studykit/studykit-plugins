# VolumetricModel.registerCustomSDFCallback Method![](../images/TestTubeLarge.png)

Parent Object: [VolumetricModel](VolumetricModel.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::volume" and the header file is <Volume/Volumetric/VolumetricModel.h>

## Description

Handling for custom Signed Distance Field callback events. These can be registered by the API client, they will provide a string ID and a handler object that implements the abstract methods. To use the callback, a GeometryGraphNodeProperty's customSDFCallbackID should be set to the same string ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"volumetricModel\_var" is a variable referencing a [VolumetricModel](VolumetricModel.htm) object.```` ``` returnValue = volumetricModel_var.registerCustomSDFCallback(id, callback) ``` ```` |

"volumetricModel\_var" is a variable referencing a [VolumetricModel](VolumetricModel.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | True if registered successfully. False otherwise. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The ID to be used in a GeometryGraphNodeProperty's customSDFCallbackID. |
| callback | [CustomSDFCallbackEventHandler](CustomSDFCallbackEventHandler.htm) | The callback object implemented by the client. |

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |