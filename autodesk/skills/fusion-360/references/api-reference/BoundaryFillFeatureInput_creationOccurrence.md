# BoundaryFillFeatureInput.creationOccurrence Property

Parent Object: [BoundaryFillFeatureInput](BoundaryFillFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeatureInput.h>

## Description

In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the Boundary Fill is created based on geometry (e.g. a profile and/or face(s)) in another component AND (the Boundary Fill) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundaryFillFeatureInput\_var" is a variable referencing a BoundaryFillFeatureInput object. |

"boundaryFillFeatureInput\_var" is a variable referencing a BoundaryFillFeatureInput object. ```` ``` #include <Fusion/Features/BoundaryFillFeatureInput.h>  // Get the value of the property. Ptr<Occurrence> propertyValue = boundaryFillFeatureInput_var->creationOccurrence();  // Set the value of the property, where value_var is an Occurrence. bool returnValue = boundaryFillFeatureInput_var->creationOccurrence(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [Occurrence](Occurrence.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Boundary Fill Feature API Sample](BoundaryFillFeatureSample_Sample.htm) | Demonstrates creating a new boundary fill feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |