# ExtendFeatureInput.isChainingEnabled Property

Parent Object: [ExtendFeatureInput](ExtendFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtendFeatureInput.h>

## Description

Gets and sets if all edges that are tangent or curvature continuous, and end point connected, will be found automatically and extended.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extendFeatureInput\_var" is a variable referencing an ExtendFeatureInput object. |

"extendFeatureInput\_var" is a variable referencing an ExtendFeatureInput object. ```` ``` #include <Fusion/Features/ExtendFeatureInput.h>  // Get the value of the property. boolean propertyValue = extendFeatureInput_var->isChainingEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = extendFeatureInput_var->isChainingEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |