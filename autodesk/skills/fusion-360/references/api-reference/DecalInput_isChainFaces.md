# DecalInput.isChainFaces Property

Parent Object: [DecalInput](DecalInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/DecalInput.h>

## Description

Controls if the decal will wrap onto the faces that connect to the face the decal is placed on. When this is true, the list of faces should contain only one face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"decalInput\_var" is a variable referencing a DecalInput object.  ```` ``` # Get the value of the property. propertyValue = decalInput_var.isChainFaces  # Set the value of the property. decalInput_var.isChainFaces = propertyValue ``` ```` |

"decalInput\_var" is a variable referencing a DecalInput object. ```` ``` #include <Fusion/Image/DecalInput.h>  // Get the value of the property. boolean propertyValue = decalInput_var->isChainFaces();  // Set the value of the property, where value_var is a boolean. bool returnValue = decalInput_var->isChainFaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |