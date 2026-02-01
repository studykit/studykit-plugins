# ScaleFeature.inputEntities Property

Parent Object: [ScaleFeature](ScaleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ScaleFeature.h>

## Description

Gets and sets the input entities. This collection can contain sketches, BRep bodies and T-Spline bodies in parametric modeling. It can contain sketches, BRep bodies, T-Spline bodies, mesh bodies, root component and occurrences in non-parametric modeling. If the scaling is non-uniform (the isUniform property is false), this collection cannot contain sketches or components.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scaleFeature\_var" is a variable referencing a ScaleFeature object.  ```` ``` # Get the value of the property. propertyValue = scaleFeature_var.inputEntities  # Set the value of the property. scaleFeature_var.inputEntities = propertyValue ``` ```` |

"scaleFeature\_var" is a variable referencing a ScaleFeature object. ```` ``` #include <Fusion/Features/ScaleFeature.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = scaleFeature_var->inputEntities();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = scaleFeature_var->inputEntities(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |