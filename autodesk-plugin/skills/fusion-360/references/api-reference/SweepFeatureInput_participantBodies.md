# SweepFeatureInput.participantBodies Property

Parent Object: [SweepFeatureInput](SweepFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeatureInput.h>

## Description

Gets and sets the list of bodies that will participate in the feature when the operation is a cut or intersection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = sweepFeatureInput_var.participantBodies  # Set the value of the property. sweepFeatureInput_var.participantBodies = propertyValue ``` ```` |

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. ```` ``` #include <Fusion/Features/SweepFeatureInput.h>  // Get the value of the property. std::vector<Ptr<BRepBody>> propertyValue = sweepFeatureInput_var->participantBodies();  // Set the value of the property, where value_var is a BRepBody. bool returnValue = sweepFeatureInput_var->participantBodies(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [BRepBody](BRepBody.htm).

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |