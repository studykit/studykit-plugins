# ExtrudeFeatureInput.participantBodies Property

Parent Object: [ExtrudeFeatureInput](ExtrudeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatureInput.h>

## Description

Gets and sets the list of bodies that will participate in the feature when the operation is a cut or intersection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeatureInput\_var" is a variable referencing an ExtrudeFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = extrudeFeatureInput_var.participantBodies  # Set the value of the property. extrudeFeatureInput_var.participantBodies = propertyValue ``` ```` |

"extrudeFeatureInput\_var" is a variable referencing an ExtrudeFeatureInput object. ```` ``` #include <Fusion/Features/ExtrudeFeatureInput.h>  // Get the value of the property. std::vector<Ptr<BRepBody>> propertyValue = extrudeFeatureInput_var->participantBodies();  // Set the value of the property, where value_var is a BRepBody. bool returnValue = extrudeFeatureInput_var->participantBodies(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [BRepBody](BRepBody.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Manage Participant Bodies API Sample](ParticipantBodiesSample_Sample.htm) | Demonstrates how to manage participant During Cut operation. Same API can be used to manage participants During intersection also. |

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |