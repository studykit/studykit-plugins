# InCanvasRendering.start Method

Parent Object: [InCanvasRendering](InCanvasRendering.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/InCanvasRendering.h>

## Description

Starts the process of in-canvas rendering. There are two modes when doing in-canvas rendering; advanced and fast. This is specified in the API using the isAdvanced property. When using advanced rendering, you can specify the desired quality and the rendering will stop once that quality has been reached. When using fast rendering, the rendering never stops but continues until you stop it.

## Syntax

* [Python](#Python)
* [C++](#C++)

"inCanvasRendering\_var" is a variable referencing an [InCanvasRendering](InCanvasRendering.htm) object.```` ``` returnValue = inCanvasRendering_var.start(renderQuality) ``` ```` |

"inCanvasRendering\_var" is a variable referencing an [InCanvasRendering](InCanvasRendering.htm) object.  ```` ``` #include <Fusion/Render/InCanvasRendering.h>  returnValue = inCanvasRendering_var->start(renderQuality); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the rendering was successfully started. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| renderQuality | double | Specifies the desired quality of the rendering. The quality is specified using a value between 0 and 1, where 0.75 is the equivalent of "Excellent" and 1.0 is the same as "Final" in the user interface.   This is ignored when using fast rendering (the isAdvanced property is False). |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |