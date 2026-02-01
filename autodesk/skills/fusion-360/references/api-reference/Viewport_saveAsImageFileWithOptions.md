# Viewport.saveAsImageFileWithOptions Method

Parent Object: [Viewport](Viewport.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Viewport.h>

## Description

Saves the current view to the specified image file. The view is re-rendered to the specified size and not just scaled from the existing view. This allows you to generate higher resolution images than you could do with just a screen capture.

## Syntax

* [Python](#Python)
* [C++](#C++)

"viewport\_var" is a variable referencing a [Viewport](Viewport.htm) object.```` ``` returnValue = viewport_var.saveAsImageFileWithOptions(options) ``` ```` |

"viewport\_var" is a variable referencing a [Viewport](Viewport.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the operation was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| options | [SaveImageFileOptions](SaveImageFileOptions.htm) | A SaveImageFileOptions object that defines the various options that define how the image should be created. The SaveImageFileOptions can be created by using the static create method on the SaveImageFileOptions class. |

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |