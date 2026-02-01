# SweepFeatureInput.solidBody Property

Parent Object: [SweepFeatureInput](SweepFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeatureInput.h>

## Description

Gets and sets the BRepBody object to sweep. It must be a solid body. Setting this property results in the type being a single path sweep, and if the profile, guide path, or surface are set, they are set to null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. |

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. ```` ``` #include <Fusion/Features/SweepFeatureInput.h>  // Get the value of the property. Ptr<BRepBody> propertyValue = sweepFeatureInput_var->solidBody();  // Set the value of the property, where value_var is a BRepBody. bool returnValue = sweepFeatureInput_var->solidBody(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BRepBody](BRepBody.htm).

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |