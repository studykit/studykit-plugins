# MirrorFeature.isCombine Property

Parent Object: [MirrorFeature](MirrorFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MirrorFeature.h>

## Description

Gets and sets whether combine is set when doing the Mirror. When true, the mirrored geometry will be Boolean unioned with the original solid or surface body(s) when they connect within the stitch tolerance defined with the stitchTolerance property. If the bodies cannot be unioned or stitched the result will be separate bodies.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mirrorFeature\_var" is a variable referencing a MirrorFeature object.  ```` ``` # Get the value of the property. propertyValue = mirrorFeature_var.isCombine  # Set the value of the property. mirrorFeature_var.isCombine = propertyValue ``` ```` |

"mirrorFeature\_var" is a variable referencing a MirrorFeature object. ```` ``` #include <Fusion/Features/MirrorFeature.h>  // Get the value of the property. boolean propertyValue = mirrorFeature_var->isCombine();  // Set the value of the property, where value_var is a boolean. bool returnValue = mirrorFeature_var->isCombine(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |