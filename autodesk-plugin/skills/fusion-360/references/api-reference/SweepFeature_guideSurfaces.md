# SweepFeature.guideSurfaces Property

Parent Object: [SweepFeature](SweepFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeature.h>

## Description

Gets and sets the guide surfaces to create the sweep. This can be set to an empty array to remove the guide surfaces and have a single path sweep feature. The isChainSelection property controls whether tangentially connected faces to the guide surfaces are also made guide surfaces.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeature\_var" is a variable referencing a SweepFeature object.  ```` ``` # Get the value of the property. propertyValue = sweepFeature_var.guideSurfaces  # Set the value of the property. sweepFeature_var.guideSurfaces = propertyValue ``` ```` |

"sweepFeature\_var" is a variable referencing a SweepFeature object. ```` ``` #include <Fusion/Features/SweepFeature.h>  // Get the value of the property. std::vector<Ptr<BRepFace>> propertyValue = sweepFeature_var->guideSurfaces();  // Set the value of the property, where value_var is a BRepFace. bool returnValue = sweepFeature_var->guideSurfaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [BRepFace](BRepFace.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |