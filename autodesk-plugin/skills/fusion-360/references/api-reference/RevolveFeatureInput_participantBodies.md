# RevolveFeatureInput.participantBodies Property

Parent Object: [RevolveFeatureInput](RevolveFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeatureInput.h>

## Description

Gets and sets the list of bodies that will participate in the feature when the operation is a cut or intersection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeatureInput\_var" is a variable referencing a RevolveFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = revolveFeatureInput_var.participantBodies  # Set the value of the property. revolveFeatureInput_var.participantBodies = propertyValue ``` ```` |

"revolveFeatureInput\_var" is a variable referencing a RevolveFeatureInput object. ```` ``` #include <Fusion/Features/RevolveFeatureInput.h>  // Get the value of the property. std::vector<Ptr<BRepBody>> propertyValue = revolveFeatureInput_var->participantBodies();  // Set the value of the property, where value_var is a BRepBody. bool returnValue = revolveFeatureInput_var->participantBodies(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [BRepBody](BRepBody.htm).

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |