# PipeFeature.participantBodies Property

Parent Object: [PipeFeature](PipeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeature.h>

## Description

Gets and sets the list of bodies that will participate in the feature when the operation is a cut or intersection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeature\_var" is a variable referencing a PipeFeature object.  ```` ``` # Get the value of the property. propertyValue = pipeFeature_var.participantBodies  # Set the value of the property. pipeFeature_var.participantBodies = propertyValue ``` ```` |

"pipeFeature\_var" is a variable referencing a PipeFeature object. ```` ``` #include <Fusion/Features/PipeFeature.h>  // Get the value of the property. std::vector<Ptr<BRepBody>> propertyValue = pipeFeature_var->participantBodies();  // Set the value of the property, where value_var is a BRepBody. bool returnValue = pipeFeature_var->participantBodies(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [BRepBody](BRepBody.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |