# DecalInput.imageFilename Property

Parent Object: [DecalInput](DecalInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/DecalInput.h>

## Description

Gets and sets the filename of the image used for the decal.

## Syntax

* [Python](#Python)
* [C++](#C++)

"decalInput\_var" is a variable referencing a DecalInput object.  ```` ``` # Get the value of the property. propertyValue = decalInput_var.imageFilename  # Set the value of the property. decalInput_var.imageFilename = propertyValue ``` ```` |

"decalInput\_var" is a variable referencing a DecalInput object. ```` ``` #include <Fusion/Image/DecalInput.h>  // Get the value of the property. string propertyValue = decalInput_var->imageFilename();  // Set the value of the property, where value_var is a string. bool returnValue = decalInput_var->imageFilename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |