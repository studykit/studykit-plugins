# PipeFeatureInput.participantBodies Property

Parent Object: [PipeFeatureInput](PipeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeatureInput.h>

## Description

Gets and sets the list of bodies that will participate in the feature when the operation is a cut or intersection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeatureInput\_var" is a variable referencing a PipeFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = pipeFeatureInput_var.participantBodies  # Set the value of the property. pipeFeatureInput_var.participantBodies = propertyValue ``` ```` |

"pipeFeatureInput\_var" is a variable referencing a PipeFeatureInput object. ```` ``` #include <Fusion/Features/PipeFeatureInput.h>  // Get the value of the property. std::vector<Ptr<BRepBody>> propertyValue = pipeFeatureInput_var->participantBodies();  // Set the value of the property, where value_var is a BRepBody. bool returnValue = pipeFeatureInput_var->participantBodies(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [BRepBody](BRepBody.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |