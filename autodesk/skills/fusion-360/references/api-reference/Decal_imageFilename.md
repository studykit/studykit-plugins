# Decal.imageFilename Property

Parent Object: [Decal](Decal.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Decal.h>

## Description

Gets and sets the filename of the image used for the decal. When getting this property, the filename returned is the file that was used when the decal was initially created. it's possible the file may no longer exist.

## Syntax

* [Python](#Python)
* [C++](#C++)

"decal\_var" is a variable referencing a Decal object.  ```` ``` # Get the value of the property. propertyValue = decal_var.imageFilename  # Set the value of the property. decal_var.imageFilename = propertyValue ``` ```` |

"decal\_var" is a variable referencing a Decal object. ```` ``` #include <Fusion/Image/Decal.h>  // Get the value of the property. string propertyValue = decal_var->imageFilename();  // Set the value of the property, where value_var is a string. bool returnValue = decal_var->imageFilename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |