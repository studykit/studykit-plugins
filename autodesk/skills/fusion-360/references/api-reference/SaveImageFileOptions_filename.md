# SaveImageFileOptions.filename Property

Parent Object: [SaveImageFileOptions](SaveImageFileOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SaveImageFileOptions.h>

## Description

Gets and sets the full filename, including the path, of the image file. The type of image file to be created is inferred from the extension of the filename.

## Syntax

* [Python](#Python)
* [C++](#C++)

"saveImageFileOptions\_var" is a variable referencing a SaveImageFileOptions object. |

"saveImageFileOptions\_var" is a variable referencing a SaveImageFileOptions object. ```` ``` #include <Core/Application/SaveImageFileOptions.h>  // Get the value of the property. string propertyValue = saveImageFileOptions_var->filename();  // Set the value of the property, where value_var is a string. bool returnValue = saveImageFileOptions_var->filename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |