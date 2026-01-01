# LoftFeatureInput.isClosed Property

Parent Object: [LoftFeatureInput](LoftFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFeatureInput.h>

## Description

Specifies if the loft closes back on itself. In other words, the first section is also used as the last section and the connection is smooth. This property defaults to false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFeatureInput\_var" is a variable referencing a LoftFeatureInput object. |

"loftFeatureInput\_var" is a variable referencing a LoftFeatureInput object. ```` ``` #include <Fusion/Features/LoftFeatureInput.h>  // Get the value of the property. boolean propertyValue = loftFeatureInput_var->isClosed();  // Set the value of the property, where value_var is a boolean. bool returnValue = loftFeatureInput_var->isClosed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |