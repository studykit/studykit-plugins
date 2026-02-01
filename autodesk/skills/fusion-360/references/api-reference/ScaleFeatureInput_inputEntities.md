# ScaleFeatureInput.inputEntities Property

Parent Object: [ScaleFeatureInput](ScaleFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ScaleFeatureInput.h>

## Description

Gets and sets the input entities. This collection can contain sketches, BRep bodies and T-Spline bodies in parametric modeling. It can contain sketches, BRep bodies, T-Spline bodies, mesh bodies, root component and occurrences in non-parametric modeling. If the scaling is non-uniform (the isUniform property is false), this collection cannot contain sketches or components.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scaleFeatureInput\_var" is a variable referencing a ScaleFeatureInput object. |

"scaleFeatureInput\_var" is a variable referencing a ScaleFeatureInput object. ```` ``` #include <Fusion/Features/ScaleFeatureInput.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = scaleFeatureInput_var->inputEntities();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = scaleFeatureInput_var->inputEntities(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |