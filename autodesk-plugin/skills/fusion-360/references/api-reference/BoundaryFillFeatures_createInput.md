# BoundaryFillFeatures.createInput Method

Parent Object: [BoundaryFillFeatures](BoundaryFillFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeatures.h>

## Description

Creates a BoundaryFillFeatureInput object. Use properties and methods on this object to define the boundary fill you want to create and then use the Add method, passing in the BoundaryFillFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundaryFillFeatures\_var" is a variable referencing a [BoundaryFillFeatures](BoundaryFillFeatures.htm) object.```` ``` returnValue = boundaryFillFeatures_var.createInput(tools, operation) ``` ```` |

"boundaryFillFeatures\_var" is a variable referencing a [BoundaryFillFeatures](BoundaryFillFeatures.htm) object.  ```` ``` #include <Fusion/Features/BoundaryFillFeatures.h>  returnValue = boundaryFillFeatures_var->createInput(tools, operation); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BoundaryFillFeatureInput](BoundaryFillFeatureInput.htm) | Returns the newly created BoundaryFillFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| tools | [ObjectCollection](ObjectCollection.htm) | A collection of one or more construction planes and open or closed BRepBody objects that will be used in calculating the possible closed boundaries. |
| operation | [FeatureOperations](FeatureOperations.htm) | The operation type to perform. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [boundaryFillFeatures.add](boundaryFillFeatures_add_Sample.htm) | Demonstrates the boundaryFill.add method. To use this sample you need to have two existing overlapping bodies. You'll be prompted to select the bodies when running the script. |
| [Boundary Fill Feature API Sample](BoundaryFillFeatureSample_Sample.htm) | Demonstrates creating a new boundary fill feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |