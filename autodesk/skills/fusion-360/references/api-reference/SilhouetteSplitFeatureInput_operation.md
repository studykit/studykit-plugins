# SilhouetteSplitFeatureInput.operation Property

Parent Object: [SilhouetteSplitFeatureInput](SilhouetteSplitFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SilhouetteSplitFeatureInput.h>

## Description

Gets and sets the type of silhouette split operation to perform.

## Syntax

* [Python](#Python)
* [C++](#C++)

"silhouetteSplitFeatureInput\_var" is a variable referencing a SilhouetteSplitFeatureInput object. |

"silhouetteSplitFeatureInput\_var" is a variable referencing a SilhouetteSplitFeatureInput object. ```` ``` #include <Fusion/Features/SilhouetteSplitFeatureInput.h>  // Get the value of the property. SilhouetteSplitOperations propertyValue = silhouetteSplitFeatureInput_var->operation();  // Set the value of the property, where value_var is a SilhouetteSplitOperations. bool returnValue = silhouetteSplitFeatureInput_var->operation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SilhouetteSplitOperations](SilhouetteSplitOperations.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |