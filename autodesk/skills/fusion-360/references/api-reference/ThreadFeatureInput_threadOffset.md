# ThreadFeatureInput.threadOffset Property

Parent Object: [ThreadFeatureInput](ThreadFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeatureInput.h>

## Description

Gets and sets the thread offset. The offset is the distance along the axis of the cylinder from the edge to the start of the thread. It is only used in the case where the isFullLength property is false. Returns nothing in the case where the feature is non-parametric.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeatureInput\_var" is a variable referencing a ThreadFeatureInput object. |

"threadFeatureInput\_var" is a variable referencing a ThreadFeatureInput object. ```` ``` #include <Fusion/Features/ThreadFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = threadFeatureInput_var->threadOffset();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = threadFeatureInput_var->threadOffset(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |