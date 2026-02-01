# BoundaryFillFeatureInput.bRepCells Property

Parent Object: [BoundaryFillFeatureInput](BoundaryFillFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeatureInput.h>

## Description

Returns the collection of the valid cells that have been calculated based on the set of input tools. You use this collection to specify which cells you want included in the output.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundaryFillFeatureInput\_var" is a variable referencing a BoundaryFillFeatureInput object. |

"boundaryFillFeatureInput\_var" is a variable referencing a BoundaryFillFeatureInput object. ```` ``` #include <Fusion/Features/BoundaryFillFeatureInput.h>  // Get the value of the property. Ptr<BRepCells> propertyValue = boundaryFillFeatureInput_var->bRepCells(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepCells](BRepCells.htm).

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