# SaveImageFileOptions.isBackgroundTransparent Property

Parent Object: [SaveImageFileOptions](SaveImageFileOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SaveImageFileOptions.h>

## Description

Gets and sets if the background should be rendered as transparent. If false, the background will be the same as seen in Fusion.

## Syntax

* [Python](#Python)
* [C++](#C++)

"saveImageFileOptions\_var" is a variable referencing a SaveImageFileOptions object.  ```` ``` # Get the value of the property. propertyValue = saveImageFileOptions_var.isBackgroundTransparent  # Set the value of the property. saveImageFileOptions_var.isBackgroundTransparent = propertyValue ``` ```` |

"saveImageFileOptions\_var" is a variable referencing a SaveImageFileOptions object. ```` ``` #include <Core/Application/SaveImageFileOptions.h>  // Get the value of the property. boolean propertyValue = saveImageFileOptions_var->isBackgroundTransparent();  // Set the value of the property, where value_var is a boolean. bool returnValue = saveImageFileOptions_var->isBackgroundTransparent(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |