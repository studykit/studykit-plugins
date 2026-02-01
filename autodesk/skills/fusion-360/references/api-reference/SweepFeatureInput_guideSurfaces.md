# SweepFeatureInput.guideSurfaces Property

Parent Object: [SweepFeatureInput](SweepFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeatureInput.h>

## Description

Gets and sets the guide surfaces to create the sweep. This can be set to an empty array to remove the guide surfaces and have a single path sweep feature. By default connected faces that are tangent to any of the guide faces are set as guide faces. Use the isChainSelection property to disable the use of tangent faces.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. |

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. ```` ``` #include <Fusion/Features/SweepFeatureInput.h>  // Get the value of the property. std::vector<Ptr<BRepFace>> propertyValue = sweepFeatureInput_var->guideSurfaces();  // Set the value of the property, where value_var is a BRepFace. bool returnValue = sweepFeatureInput_var->guideSurfaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [BRepFace](BRepFace.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |