# SaveImageFileOptions.create Method

Parent Object: [SaveImageFileOptions](SaveImageFileOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SaveImageFileOptions.h>

## Description

Creates a new SaveImageFileOptions object. The returned object can be used to define the various options to use when saving a viewport as an image. The object is passed into the ViewPort.saveAsImageFileWithOptions method to create an image of the viewport.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SaveImageFileOptions](SaveImageFileOptions.htm) | Returns a SaveImageFileOptions object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filename | string | The full filename, including the path, of the image file. The type of image file to be created is inferred from the extension of the filename. |

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |