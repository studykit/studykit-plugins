# SaveImageFileOptions.height Property

Parent Object: [SaveImageFileOptions](SaveImageFileOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SaveImageFileOptions.h>

## Description

Gets and set the height of the image to be created in pixels. A value of zero is valid and indicates the current height of the viewport is to be used. When the SaveImageFileOptions object is initially created, this is initialized to 0.

## Syntax

* [Python](#Python)
* [C++](#C++)

"saveImageFileOptions\_var" is a variable referencing a SaveImageFileOptions object. |

"saveImageFileOptions\_var" is a variable referencing a SaveImageFileOptions object. ```` ``` #include <Core/Application/SaveImageFileOptions.h>  // Get the value of the property. integer propertyValue = saveImageFileOptions_var->height();  // Set the value of the property, where value_var is an integer. bool returnValue = saveImageFileOptions_var->height(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |