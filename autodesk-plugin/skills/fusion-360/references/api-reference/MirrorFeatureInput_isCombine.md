# MirrorFeatureInput.isCombine Property

Parent Object: [MirrorFeatureInput](MirrorFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MirrorFeatureInput.h>

## Description

Gets and sets whether the mirrored bodies should be combined with the original bodies. When true, the mirrored geometry will be Boolean unioned with the original solid or surface body(s) when they connect within the stitch tolerance defined with the stitchTolerance property. If the bodies cannot be unioned or stitched the result will be separate bodies. If any input object is not a body, then this setting is ignored. Default is false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mirrorFeatureInput\_var" is a variable referencing a MirrorFeatureInput object. |

"mirrorFeatureInput\_var" is a variable referencing a MirrorFeatureInput object. ```` ``` #include <Fusion/Features/MirrorFeatureInput.h>  // Get the value of the property. boolean propertyValue = mirrorFeatureInput_var->isCombine();  // Set the value of the property, where value_var is a boolean. bool returnValue = mirrorFeatureInput_var->isCombine(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |