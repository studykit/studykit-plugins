# Decal.saveImage Method

Parent Object: [Decal](Decal.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Decal.h>

## Description

Saves the image associated with the decal to the specified file. This is useful in cases where the original image file is no longer available but you need the image for some other purpose.

## Syntax

* [Python](#Python)
* [C++](#C++)

"decal\_var" is a variable referencing a [Decal](Decal.htm) object.```` ``` returnValue = decal_var.saveImage(filename) ``` ```` |

"decal\_var" is a variable referencing a [Decal](Decal.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if writing the file was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filename | string | The full filename of the image to save, including the extension of the file, which controls what format the image file will be. If file extension is other than png, jpg or tiff, then by default png extension will be added to the filename. This method will fail if a file with the specified filename already exists. If you want to overwrite the file, you'll need to delete it first before calling this method. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |