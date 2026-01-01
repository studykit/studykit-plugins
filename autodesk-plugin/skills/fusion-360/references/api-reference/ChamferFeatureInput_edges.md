# ChamferFeatureInput.edges Property

Parent Object: [ChamferFeatureInput](ChamferFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferFeatureInput.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferFeatureInput\_var" is a variable referencing a ChamferFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = chamferFeatureInput_var.edges  # Set the value of the property. chamferFeatureInput_var.edges = propertyValue ``` ```` |

"chamferFeatureInput\_var" is a variable referencing a ChamferFeatureInput object. ```` ``` #include <Fusion/Features/ChamferFeatureInput.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = chamferFeatureInput_var->edges();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = chamferFeatureInput_var->edges(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version November 2014
Retired in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |