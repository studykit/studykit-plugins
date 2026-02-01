# Canvas.saveImage Method

Parent Object: [Canvas](Canvas.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Canvas.h>

## Description

Saves the image associated with the canvas to the specified file. This is useful in cases where the original image file is no longer available but you need the image for some other purpose.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvas\_var" is a variable referencing a [Canvas](Canvas.htm) object.```` ``` returnValue = canvas_var.saveImage(filename) ``` ```` |

"canvas\_var" is a variable referencing a [Canvas](Canvas.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if writing the file was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filename | string | The full filename of the image to save, including the file extension, which controls the format of the image file. If a file extension other than png, jpg, or tiff is specified, a png extension will be added to the filename by default.   This method will fail if a file with the specified filename already exists. If you want to overwrite the file, you'll need to delete it first before calling this method. |

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |