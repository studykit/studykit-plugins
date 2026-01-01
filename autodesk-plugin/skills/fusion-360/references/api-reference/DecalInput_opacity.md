# DecalInput.opacity Property

Parent Object: [DecalInput](DecalInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/DecalInput.h>

## Description

Gets and sets the opacity of the decal where 0 is completely transparent and 1.0 is completely opaque. Setting this property to a value outside the range of 0-1 will result in the value being set to the closest valid value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"decalInput\_var" is a variable referencing a DecalInput object.  ```` ``` # Get the value of the property. propertyValue = decalInput_var.opacity  # Set the value of the property. decalInput_var.opacity = propertyValue ``` ```` |

"decalInput\_var" is a variable referencing a DecalInput object. ```` ``` #include <Fusion/Image/DecalInput.h>  // Get the value of the property. double propertyValue = decalInput_var->opacity();  // Set the value of the property, where value_var is a double. bool returnValue = decalInput_var->opacity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |