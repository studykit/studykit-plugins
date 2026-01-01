# BRepCell.isSelected Property

Parent Object: [BRepCell](BRepCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BRepCell.h>

## Description

Gets and sets whether the cell is selected. For a Trim feature a selected cell is removed, whereas for a boundary fill feature, a selected cell is kept and used in the feature operation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCell\_var" is a variable referencing a BRepCell object. |

"bRepCell\_var" is a variable referencing a BRepCell object. ```` ``` #include <Fusion/Features/BRepCell.h>  // Get the value of the property. boolean propertyValue = bRepCell_var->isSelected();  // Set the value of the property, where value_var is a boolean. bool returnValue = bRepCell_var->isSelected(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [boundaryFillFeatures.add](boundaryFillFeatures_add_Sample.htm) | Demonstrates the boundaryFill.add method. To use this sample you need to have two existing overlapping bodies. You'll be prompted to select the bodies when running the script. |
| [Boundary Fill Feature API Sample](BoundaryFillFeatureSample_Sample.htm) | Demonstrates creating a new boundary fill feature. |
| [Trim Feature API Sample](TrimFeatureSample_Sample.htm) | Demonstrates creating a new trim feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |