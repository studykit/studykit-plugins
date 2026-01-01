# SaveImageFileOptions.isAntiAliased Property

Parent Object: [SaveImageFileOptions](SaveImageFileOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SaveImageFileOptions.h>

## Description

Gets and sets if the rendered image should be anti-aliased or not. If false, there is no anti-aliasing.

## Syntax

* [Python](#Python)
* [C++](#C++)

"saveImageFileOptions\_var" is a variable referencing a SaveImageFileOptions object.  ```` ``` # Get the value of the property. propertyValue = saveImageFileOptions_var.isAntiAliased  # Set the value of the property. saveImageFileOptions_var.isAntiAliased = propertyValue ``` ```` |

"saveImageFileOptions\_var" is a variable referencing a SaveImageFileOptions object. ```` ``` #include <Core/Application/SaveImageFileOptions.h>  // Get the value of the property. boolean propertyValue = saveImageFileOptions_var->isAntiAliased();  // Set the value of the property, where value_var is a boolean. bool returnValue = saveImageFileOptions_var->isAntiAliased(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |