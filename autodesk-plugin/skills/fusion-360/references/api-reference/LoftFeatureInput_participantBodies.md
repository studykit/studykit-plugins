# LoftFeatureInput.participantBodies Property

Parent Object: [LoftFeatureInput](LoftFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFeatureInput.h>

## Description

Gets and sets the list of bodies that will participate in the feature when the operation is a cut or intersection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFeatureInput\_var" is a variable referencing a LoftFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = loftFeatureInput_var.participantBodies  # Set the value of the property. loftFeatureInput_var.participantBodies = propertyValue ``` ```` |

"loftFeatureInput\_var" is a variable referencing a LoftFeatureInput object. ```` ``` #include <Fusion/Features/LoftFeatureInput.h>  // Get the value of the property. std::vector<Ptr<BRepBody>> propertyValue = loftFeatureInput_var->participantBodies();  // Set the value of the property, where value_var is a BRepBody. bool returnValue = loftFeatureInput_var->participantBodies(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [BRepBody](BRepBody.htm).

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |