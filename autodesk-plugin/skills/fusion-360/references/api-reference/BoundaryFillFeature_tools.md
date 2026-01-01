# BoundaryFillFeature.tools Property

Parent Object: [BoundaryFillFeature](BoundaryFillFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeature.h>

## Description

A collection of construction planes and open or closed BRepBody objects that define the set of boundaries that have been used in the calculation of available closed boundaries. Setting this property will clear all currently selected tools.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundaryFillFeature\_var" is a variable referencing a BoundaryFillFeature object.  ```` ``` # Get the value of the property. propertyValue = boundaryFillFeature_var.tools  # Set the value of the property. boundaryFillFeature_var.tools = propertyValue ``` ```` |

"boundaryFillFeature\_var" is a variable referencing a BoundaryFillFeature object. ```` ``` #include <Fusion/Features/BoundaryFillFeature.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = boundaryFillFeature_var->tools();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = boundaryFillFeature_var->tools(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |