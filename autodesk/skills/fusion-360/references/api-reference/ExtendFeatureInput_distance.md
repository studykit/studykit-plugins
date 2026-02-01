# ExtendFeatureInput.distance Property

Parent Object: [ExtendFeatureInput](ExtendFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtendFeatureInput.h>

## Description

Gets and sets the ValueInput object that defines the extend distance

## Syntax

* [Python](#Python)
* [C++](#C++)

"extendFeatureInput\_var" is a variable referencing an ExtendFeatureInput object. |

"extendFeatureInput\_var" is a variable referencing an ExtendFeatureInput object. ```` ``` #include <Fusion/Features/ExtendFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = extendFeatureInput_var->distance();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = extendFeatureInput_var->distance(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |