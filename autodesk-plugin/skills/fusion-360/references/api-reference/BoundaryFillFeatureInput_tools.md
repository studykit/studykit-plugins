# BoundaryFillFeatureInput.tools Property

Parent Object: [BoundaryFillFeatureInput](BoundaryFillFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeatureInput.h>

## Description

Gets and sets the collection of one or more construction planes and open or closed BRepBody objects that are used in calculating the possible closed boundaries.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundaryFillFeatureInput\_var" is a variable referencing a BoundaryFillFeatureInput object. |

"boundaryFillFeatureInput\_var" is a variable referencing a BoundaryFillFeatureInput object. ```` ``` #include <Fusion/Features/BoundaryFillFeatureInput.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = boundaryFillFeatureInput_var->tools();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = boundaryFillFeatureInput_var->tools(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |