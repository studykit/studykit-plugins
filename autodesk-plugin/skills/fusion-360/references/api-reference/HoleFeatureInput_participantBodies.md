# HoleFeatureInput.participantBodies Property

Parent Object: [HoleFeatureInput](HoleFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeatureInput.h>

## Description

Gets and sets the list of bodies that will participate in the hole.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeatureInput\_var" is a variable referencing a HoleFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = holeFeatureInput_var.participantBodies  # Set the value of the property. holeFeatureInput_var.participantBodies = propertyValue ``` ```` |

"holeFeatureInput\_var" is a variable referencing a HoleFeatureInput object. ```` ``` #include <Fusion/Features/HoleFeatureInput.h>  // Get the value of the property. std::vector<Ptr<BRepBody>> propertyValue = holeFeatureInput_var->participantBodies();  // Set the value of the property, where value_var is a BRepBody. bool returnValue = holeFeatureInput_var->participantBodies(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [BRepBody](BRepBody.htm).

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |