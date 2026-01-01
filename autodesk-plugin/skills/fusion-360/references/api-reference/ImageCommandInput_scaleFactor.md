# ImageCommandInput.scaleFactor Property

Parent Object: [ImageCommandInput](ImageCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ImageCommandInput.h>

## Description

Gets and sets the scale of the image. This defaults to 1.0, which is full-scale.

## Syntax

* [Python](#Python)
* [C++](#C++)

"imageCommandInput\_var" is a variable referencing an ImageCommandInput object. |

"imageCommandInput\_var" is a variable referencing an ImageCommandInput object. ```` ``` #include <Core/UserInterface/ImageCommandInput.h>  // Get the value of the property. double propertyValue = imageCommandInput_var->scaleFactor();  // Set the value of the property, where value_var is a double. bool returnValue = imageCommandInput_var->scaleFactor(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |