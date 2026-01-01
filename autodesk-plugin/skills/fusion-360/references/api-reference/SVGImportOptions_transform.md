# SVGImportOptions.transform Property

Parent Object: [SVGImportOptions](SVGImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SVGImportOptions.h>

## Description

Gets and sets the transformation matrix that defines the position, orientation, scale, and mirroring of the imported SVG data relative to the sketch coordinate system. This property defaults to an identity matrix in a newly created SVGImportOptions object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sVGImportOptions\_var" is a variable referencing a SVGImportOptions object.  ```` ``` # Get the value of the property. propertyValue = sVGImportOptions_var.transform  # Set the value of the property. sVGImportOptions_var.transform = propertyValue ``` ```` |

"sVGImportOptions\_var" is a variable referencing a SVGImportOptions object. ```` ``` #include <Core/Application/SVGImportOptions.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = sVGImportOptions_var->transform();  // Set the value of the property, where value_var is a Matrix3D. bool returnValue = sVGImportOptions_var->transform(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |