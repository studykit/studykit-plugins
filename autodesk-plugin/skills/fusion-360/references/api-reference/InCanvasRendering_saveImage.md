# InCanvasRendering.saveImage Method

Parent Object: [InCanvasRendering](InCanvasRendering.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/InCanvasRendering.h>

## Description

Saves the image as it currently exists in the active viewport. To get the best quality, this should be called after the renderComplete event has fired.

## Syntax

* [Python](#Python)
* [C++](#C++)

"inCanvasRendering\_var" is a variable referencing an [InCanvasRendering](InCanvasRendering.htm) object.```` ``` returnValue = inCanvasRendering_var.saveImage(filename) ``` ```` |

"inCanvasRendering\_var" is a variable referencing an [InCanvasRendering](InCanvasRendering.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the save was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filename | string | The filename to save the image to. This must be the full path. The file extension can be .png, .jpg, .jpeg, or .tiff and the file will be saved as that type.   The size of the image is dependent on the size of the viewport and the current specified aspect ratio. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |