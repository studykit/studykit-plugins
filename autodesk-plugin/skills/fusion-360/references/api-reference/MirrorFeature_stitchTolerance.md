# MirrorFeature.stitchTolerance Property

Parent Object: [MirrorFeature](MirrorFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MirrorFeature.h>

## Description

Returns the parameter controlling the Stitch tolerance to use when stitching mirrored surface bodies with the original bodies. You can edit the tolerance by editing the value of the parameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mirrorFeature\_var" is a variable referencing a MirrorFeature object. |

"mirrorFeature\_var" is a variable referencing a MirrorFeature object. ```` ``` #include <Fusion/Features/MirrorFeature.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = mirrorFeature_var->stitchTolerance(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |