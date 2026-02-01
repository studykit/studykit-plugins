# HoleFeature.participantBodies Property

Parent Object: [HoleFeature](HoleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeature.h>

## Description

Gets and sets the list of bodies that will participate in the feature when the operation is a cut or intersection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeature\_var" is a variable referencing a HoleFeature object.  ```` ``` # Get the value of the property. propertyValue = holeFeature_var.participantBodies  # Set the value of the property. holeFeature_var.participantBodies = propertyValue ``` ```` |

"holeFeature\_var" is a variable referencing a HoleFeature object. ```` ``` #include <Fusion/Features/HoleFeature.h>  // Get the value of the property. std::vector<Ptr<BRepBody>> propertyValue = holeFeature_var->participantBodies();  // Set the value of the property, where value_var is a BRepBody. bool returnValue = holeFeature_var->participantBodies(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [BRepBody](BRepBody.htm).

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |